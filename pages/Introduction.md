---
layout: section
---

# Part 1
## 为什么需要智慧能源？

<!-- 从一个现实问题引入：电力是怎么"用不好"的？ -->

---
layout: default
---

# 能源系统正面临前所未有的挑战

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

### 三大核心矛盾

**① 供需不确定性上升**
- 风能、光伏出力随天气剧烈波动
- 2023年全球弃风弃光损失超过 **150 TWh**

**② 需求侧日趋复杂**
- 电动汽车充电、数据中心用电急增
- 用电峰谷差不断扩大

**③ 传统方法力不从心**
- 统计模型（ARIMA）难以捕捉非线性规律
- 物理模型对实时变化响应滞后

</div>

<div class="flex flex-col justify-center">

```
传统方式：
历史数据 → 统计规律 → 预测
         （线性假设）

深度学习方式：
历史数据 ┐
天气数据 ├→ 神经网络 → 精准预测
节假日  ┘  （自动学习
            非线性模式）
```

<div class="mt-4 text-sm text-gray-500">
📌 深度学习的核心优势：<br>
自动从海量数据中提取复杂特征
</div>

</div>
</div>

<!-- 强调：不是为了用深度学习而用，而是问题本身驱动了技术选择 -->

---
layout: default
---

# 智慧能源的核心任务：时序预测

<div class="mt-4">

能源系统中最关键的数据形式是**时间序列**——数值随时间连续变化。

</div>

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="border rounded-lg p-3 text-center">
  <div class="text-2xl mb-2">⚡</div>
  <div class="font-bold">电力负荷预测</div>
  <div class="text-sm text-gray-500 mt-1">预测未来1小时～7天的用电需求，支撑电网调度</div>
</div>

<div class="border rounded-lg p-3 text-center">
  <div class="text-2xl mb-2">☀️</div>
  <div class="font-bold">可再生能源预测</div>
  <div class="text-sm text-gray-500 mt-1">预测光伏、风电出力，提升并网消纳能力</div>
</div>

<div class="border rounded-lg p-3 text-center">
  <div class="text-2xl mb-2">🔍</div>
  <div class="font-bold">异常检测</div>
  <div class="text-sm text-gray-500 mt-1">识别电力设备异常用电、偷电行为</div>
</div>

</div>

<div class="mt-6 border-l-4 border-blue-400 pl-4">

**为什么选 LSTM 和 Transformer？**

时序数据有两个关键特性：**时间顺序性**（先后有因果）和**长程依赖**（今天的用电受昨天影响）。
LSTM 和 Transformer 分别从不同角度解决了这两个问题。

</div>

<!-- 为后两部分做铺垫：先明确"要解决什么问题"，再讲"用什么工具" -->

---
layout: default
---

# 从 RNN 的困境说起

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

### RNN 的理论与现实

RNN（循环神经网络）是处理序列数据的经典方法，核心思想是：

> 每一步的输出，既依赖当前输入，也依赖上一步的**隐藏状态** $h_{t-1}$

$$h_t = \tanh(W_h h_{t-1} + W_x x_t + b)$$

**问题：梯度消失**

序列越长，早期信息在反向传播时梯度指数级衰减，模型实际上"遗忘"了很久之前的信息。

</div>

<div>

### 用一个比喻理解

想象你在读一篇长报告：
- **RNN**：读完就忘，只记得最后几段
- **LSTM**：有便利贴，重要内容主动记下来，不重要的随时划掉
- **Transformer**：把整篇报告摊开，同时扫一遍，注意力直接聚焦关键段落

</div>
</div>

<!--
这页是过渡页，帮助听众建立直觉理解，然后自然引出LSTM和Transformer
-->
