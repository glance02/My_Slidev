---
layout: default
---

# 短期电力负荷预测项目

在github上可以找到许多[基于LSTM的电力负荷预测项目](https://github.com/CubeStar1/LoadPredictor)，以下是一个典型的项目结构：

<img src="/img/lstm_dark.png" class="h-80 mx-auto"> 

<!-- ![](/img/lstm_dark.png) -->

---
layout: center
---

# LSTM 应用案例：LoadPredictor

<div class="mt-6">

**LoadPredictor** 是一个基于真实电网数据的短期负荷预测项目，数据来自**德里邦电力调度中心（Delhi SLDC）**，通过爬虫实时抓取，覆盖德里地区工业、商业与居民综合用电。

</div>

<div class="mt-8 flex gap-6 justify-center">

<div class="border rounded-xl px-8 py-5 text-center w-40">
  <div class="text-3xl mb-2">📥</div>
  <div class="font-bold">输入</div>
  <div class="text-sm text-gray-500 mt-1">过去 10 天<br>逐小时负荷</div>
</div>

<div class="flex items-center text-2xl text-gray-300">→</div>

<div class="border rounded-xl px-8 py-5 text-center w-40">
  <div class="text-3xl mb-2">🧠</div>
  <div class="font-bold">LSTM 模型</div>
  <div class="text-sm text-gray-500 mt-1">TensorFlow<br>Keras 实现</div>
</div>

<div class="flex items-center text-2xl text-gray-300">→</div>

<div class="border rounded-xl px-8 py-5 text-center w-40">
  <div class="text-3xl mb-2">📤</div>
  <div class="font-bold">输出</div>
  <div class="text-sm text-gray-500 mt-1">未来 24 小时<br>负荷预测</div>
</div>

<div class="flex items-center text-2xl text-gray-300">→</div>

<div class="border rounded-xl px-8 py-5 text-center w-40">
  <div class="text-3xl mb-2">🌐</div>
  <div class="font-bold">可视化</div>
  <div class="text-sm text-gray-500 mt-1">Streamlit<br>交互网页</div>
</div>

</div>

---
layout: default
---

# 数据处理：从网页到训练样本

<div class="mt-4 text-sm text-gray-500">通过 BeautifulSoup 爬取 Delhi SLDC 官网负荷数据，经归一化后构建滑动窗口样本。</div>

```python
from bs4 import BeautifulSoup
from sklearn.preprocessing import MinMaxScaler

# 1. 爬取原始数据
response = requests.get("https://www.delhisldc.org/Loaddata.aspx")
soup = BeautifulSoup(response.text, "html.parser")

# 2. 归一化到 [0, 1]
scaler = MinMaxScaler()
data = scaler.fit_transform(df[["load"]])

# 3. 滑动窗口切片：输入240步，预测24步
LOOK_BACK, PRED_STEPS = 240, 24

X, y = [], []
for i in range(len(data) - LOOK_BACK - PRED_STEPS):
    X.append(data[i : i + LOOK_BACK])
    y.append(data[i + LOOK_BACK : i + LOOK_BACK + PRED_STEPS])
```

<div class="mt-4 text-sm text-gray-500">
预测完成后调用 <code>scaler.inverse_transform()</code> 将结果还原为真实 MW 数值。
</div>

---
layout: center
---

# 模型结构：两层堆叠 LSTM

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(240, 1)),
    Dropout(0.2),
    LSTM(64),
    Dropout(0.2),
    Dense(24)   # 一次输出未来 24 步
])

model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)
```

<div class="mt-6 flex gap-4 items-center justify-center text-sm">

<div class="border rounded-lg px-4 py-3 text-center bg-blue-50">
  <div class="font-bold">LSTM Layer 1</div>
  <div class="text-gray-500">128 units<br>输出每步隐状态</div>
</div>
<div class="text-gray-300">→</div>
<div class="border rounded-lg px-4 py-3 text-center">
  <div class="font-bold">Dropout 0.2</div>
  <div class="text-gray-500">防止过拟合</div>
</div>
<div class="text-gray-300">→</div>
<div class="border rounded-lg px-4 py-3 text-center bg-blue-50">
  <div class="font-bold">LSTM Layer 2</div>
  <div class="text-gray-500">64 units<br>整合全局趋势</div>
</div>
<div class="text-gray-300">→</div>
<div class="border rounded-lg px-4 py-3 text-center">
  <div class="font-bold">Dropout 0.2</div>
  <div class="text-gray-500">防止过拟合</div>
</div>
<div class="text-gray-300">→</div>
<div class="border rounded-lg px-4 py-3 text-center bg-green-50">
  <div class="font-bold">Dense(24)</div>
  <div class="text-gray-500">输出24步预测</div>
</div>

</div>

---
layout: default
---

# 预测效果
 
<div class="mt-6">
 
| 指标 | **本项目 LSTM** | ARIMA |
|------|:--------------:|:-----:|
| 预测范围 | 未来 24 小时 | 未来 24 小时 |
| 输入窗口 | 过去 10 天（240步） | 过去数天 |
| RMSE | **±50 MW 量级** | ±180 MW 量级 |
| MAPE | **< 1.5%** | ~3.5% |
| 非线性建模 | ✓ | ✗ |
| 长期依赖捕捉 | ✓ | ✗ |
 
</div>
 
<div class="mt-4 text-sm text-gray-500">
 
* 负荷基线约 4000 ~ 6000 MW；ARIMA 数据为同类研究典型水平，仅供量级参考。
* ±50 MW 的误差相当于一个中型居民区的用电波动，在电网调度层面属于工程可接受范围。
 
</div>

<!--
建议这页直接切换到浏览器做 Live Demo
-->
