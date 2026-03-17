---
layout: section
---

# Part 2
## LSTM 与智慧能源

<!-- LSTM：给RNN装上了"记忆门"，让模型学会有选择地遗忘与记忆 -->

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
