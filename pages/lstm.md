---
layout: section
---

# Part 2
## LSTM 与智慧能源

<!--
LSTM：给RNN装上了"记忆门"，让模型学会有选择地遗忘与记忆
-->

---
layout: center
---

# LSTM 的直觉解释

LSTM的设计或多或少的借鉴了人类对于自然语言处理的直觉性经验

先阅读一下一个（虚构的）淘宝评论:

>“这个笔记本非常棒，纸很厚，料很足，用笔写起来手感非常舒服，而且没有一股刺鼻的油墨味；

>更加好的是这个笔记本不但便宜还做工优良，我上次在别家买的笔记本裁纸都裁不好，还会割伤手……”

看完这段话以后马上转述，会得到如下几个关键词：

“**纸好**”，“**没味道**”，“**便宜**”和“**做工好**”


---
layout: center
---

# LSTM直觉解释的特点

- 在一个时间序列中，不是所有信息都是同等有效的，大多数情况存在“关键词”或者“关键帧”
- 我们会在从头到尾阅读的时候“自动”概括已阅部分的内容并且用之前的内容帮助理解后文

基于以上这两点，LSTM的设计者提出了“长短期记忆”的概念：

**只有一部分的信息需要长期的记忆，而有的信息可以不记下来**。

同时，我们还需要一套机制可以动态的处理神经网络的“记忆”，因为有的信息可能一开始价值很高，后面价值逐渐衰减，这时候我们也需要让神经网络学会“遗忘”特定的信息

---
layout: default
---

# LSTM 的核心设计：三个门

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

LSTM（Long Short-Term Memory，长短期记忆网络）由 Hochreiter & Schmidhuber 于 **1997** 年提出，核心在于引入**细胞状态** $C_t$ 和三个门控机制：

**① 遗忘门** $f_t$：决定丢弃什么旧记忆

$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$

**② 输入门** $i_t$：决定写入什么新信息

$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$

**③ 输出门** $o_t$：决定输出什么内容

$$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$

细胞状态更新：
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$

</div>

<div class="flex flex-col justify-center text-sm">

```
         ┌──────────────────────────────┐
         │         细胞状态 C_t          │
         │  ×(遗忘) ──────────── +(写入) │
         └──────┬──────────────────┬────┘
                │                  │
         遗忘门 f_t             输入门 i_t
                │                  │
         ┌──────┴──────────────────┴────┐
x_t ───→ │   [h_{t-1}, x_t] 拼接输入    │ ───→ h_t
h_{t-1}─→│                              │
         └──────────────────────────────┘
                      ↑ 输出门 o_t
```

<div class="mt-3 text-gray-500">
🔑 关键洞察：细胞状态像"高速公路"，梯度可以直接流过，有效缓解梯度消失
</div>

</div>
</div>

<!-- 重点讲三个门的直觉，不要陷入公式细节 -->

---
layout: default
---

# LSTM 应用案例：短期电力负荷预测

<div class="mt-2">

**任务描述**：给定过去 24 小时的用电量（含天气、节假日信息），预测未来 1~24 小时的负荷。

</div>

<div class="grid grid-cols-2 gap-6 mt-3">

<div>

### 数据特征

典型输入特征向量 $\mathbf{x}_t$：

| 特征 | 说明 |
|------|------|
| 历史负荷 | 过去 T 步用电量 |
| 温度 | 对空调用电影响显著 |
| 小时/星期 | 周期性规律 |
| 节假日标志 | 用电行为异常 |

<div class="mt-3 text-sm text-gray-400 border-l-4 border-cyan-400/70 pl-3">
参考：Wang et al., 2023, <em>Frontiers in Energy Research</em> —— 多层空洞 LSTM + 注意力，MAPE 降至 <strong>1.8%</strong>
</div>

</div>

<div>

### 模型结构

````md magic-move
```python
import torch
import torch.nn as nn

class EnergyLSTM(nn.Module):
    def __init__(self, input_size=8,
                 hidden_size=128,
                 num_layers=2,
                 output_size=24):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2
        )
        self.fc = nn.Linear(hidden_size,output_size)
```

```python
class EnergyLSTM(nn.Module):
    def __init__(self, input_size=8,hidden_size=128,
                 num_layers=2,output_size=24):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2
        )
        self.fc = nn.Linear(hidden_size,output_size)
    def forward(self, x):
        # x: (batch, seq_len, features)
        out, _ = self.lstm(x)
        # 取最后一步输出
        return self.fc(out[:, -1, :])
```
````
</div>
</div>

<!--
代码尽量简洁，帮助听众理解结构，不需要逐行讲
-->

---
layout: default
---

# 短期电力负荷预测项目

在github上可以找到许多基于LSTM的电力负荷预测项目，以下是一个典型的项目结构：

![](/img/lstm_dark.png)


---
layout: default
---

# LSTM 的局限与改进方向

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### LSTM 的固有局限

**① 顺序计算，无法并行**
- 必须逐步处理时序，训练慢
- 长序列（>500步）仍有信息衰减

**② 多变量关系建模较弱**
- 难以同时捕捉多个传感器/节点之间的空间关联

**③ 超参数敏感**
- 隐藏层大小、层数、dropout 需要仔细调优

</div>

<div>

### 工程中的改进方案

| 问题 | 解决方案 |
|------|---------|
| 遗忘长期依赖 | 加入 **Attention 机制** |
| 特征提取弱 | 前置 **CNN** 提取局部模式 |
| 多节点空间关系 | 结合 **图神经网络 (GNN)** |
| 数据量少 | 使用 **迁移学习** 迁移预训练权重 |

<div class="mt-3 border-l-4 border-orange-400 pl-3 text-sm">

💡 这些改进思路，其实正在指向下一个模型——**Transformer**，它用注意力机制从根本上重构了序列建模的方式。

</div>

</div>
</div>

<!-- 自然过渡到Transformer：局限性引出下一个方案 -->
