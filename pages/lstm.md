---
layout: section
---

# Part 2
## LSTM 与智慧能源

<!--
认真听课的同学肯定会注意到这个模型是老师上课讲过的模型，我们组在老师讲到这里之前，已经找好了相关的资料，所以会在老师讲解的基础上增加一些深度和宽度
-->

---
layout: two-cols
class: my-auto
---

# 从 RNN 的困境说起

### RNN 的理论与现实

RNN（循环神经网络）是处理序列数据的经典方法，核心思想是：

> 每一步的输出，既依赖当前输入，也依赖上一步的**隐藏状态** $h_{t-1}$

$$h_t = \tanh(W_h h_{t-1} + W_x x_t + b)$$

**问题：梯度消失**

序列越长，早期信息在反向传播时梯度指数级衰减，模型实际上"遗忘"了很久之前的信息。

::right::

<FullscreenImg src="/img/lstm/RNN.png" class="h-80 m-6 rounded-xl" />

<!--
如何解决这个问题呢？
-->

---
layout: center
---

# LSTM 的直觉解释

LSTM的设计或多或少的借鉴了人类对于自然语言处理的直觉性经验

先阅读一下一个（虚构的）淘宝评论:
<Fullscreen>

**“这个笔记本非常棒，纸很厚，料很足，用笔写起来手感非常舒服，而且没有一股刺鼻的油墨味；更加好的是这个笔记本不但便宜还做工优良，我上次在别家买的笔记本裁纸都裁不好，还会割伤手……”**

</Fullscreen>

看完这段话以后马上转述，会得到如下几个关键词：

“**纸好**”，“**没味道**”，“**便宜**”和“**做工好**”

<!--
如果是让我们自己去复述，其过程应该回事什么样子呢？

会先总结出几个关键词，然后重新组织语言
-->

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

# hide: true
---

<div class="aspect-video rounded-xl shadow-2xl overflow-hidden border border-gray-700 mb-100 ">
  <iframe
    src="//player.bilibili.com/player.html?isOutside=true&aid=808976670&bvid=BV1Z34y1k7mc&cid=506125891&p=1&autoplay=0"
    allowfullscreen="true"
    class="w-full h-full"
  ></iframe>
</div>

<!--
看到3.30

记日记这个解释真的非常绝
-->

---
layout: default
---

# LSTM 的核心设计：三个门

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

LSTM（Long Short-Term Memory，长短期记忆网络）由 Hochreiter & Schmidhuber 于 **1997** 年提出，核心在于引入**细胞状态** $C_t$ 和三个门控机制：

**① 遗忘门** $\mathbf{F}_t$：决定丢弃什么旧记忆

$$\mathbf{F}_t = \sigma(\mathbf{X}_t \mathbf{W}_{xf} + \mathbf{H}_{t-1} \mathbf{W}_{hf} + \mathbf{b}_f)$$

**② 输入门** $\mathbf{I}_t$：决定写入什么新信息

$$\mathbf{I}_t = \sigma(\mathbf{X}_t \mathbf{W}_{xi} + \mathbf{H}_{t-1} \mathbf{W}_{hi} + \mathbf{b}_i)$$

**③ 输出门** $\mathbf{O}_t$：决定输出什么内容

$$\mathbf{O}_t = \sigma(\mathbf{X}_t \mathbf{W}_{xo} + \mathbf{H}_{t-1} \mathbf{W}_{ho} + \mathbf{b}_o)$$

**细胞状态**$\mathbf{C}_t$更新：

$$\mathbf{C}_t = \mathbf{F}_t \odot \mathbf{C}_{t-1} + \mathbf{I}_t \odot \tilde{\mathbf{C}}_t.$$


</div>

<div>

<FullscreenImg src="/img/lstm/lstm.svg" class="h-60 mx-auto rounded-lg my-12 bg-white" />

<div class="mt-6 text-gray-500">
🔑 关键洞察：细胞状态像"高速公路"，梯度可以直接流过，有效缓解梯度消失
</div>

</div>

</div>

<!--
这些公式和这张图片都是出于李沐老师的《动手深度学习》中的开源代码。

lstm是一个比较简单的模型，代码实现也比较简洁，所以在此展示一部分模型代码。
-->

---
layout: default
hide: true
---

## LoadPredictor具体部署

<iframe 
  src="https://lstm-show.streamlit.app/?embed=true" 
  width="100%" 
  height="450" 
  frameborder="0">
</iframe>


---
layout: two-cols
class: my-auto
---

# lstm的代码实现

**① 遗忘门** $\mathbf{F}_t$：决定丢弃什么旧记忆

$$\mathbf{F}_t = \sigma(\mathbf{X}_t \mathbf{W}_{xf} + \mathbf{H}_{t-1} \mathbf{W}_{hf} + \mathbf{b}_f)$$

**② 输入门** $\mathbf{I}_t$：决定写入什么新信息

$$\mathbf{I}_t = \sigma(\mathbf{X}_t \mathbf{W}_{xi} + \mathbf{H}_{t-1} \mathbf{W}_{hi} + \mathbf{b}_i)$$

**③ 输出门** $\mathbf{O}_t$：决定输出什么内容

$$\mathbf{O}_t = \sigma(\mathbf{X}_t \mathbf{W}_{xo} + \mathbf{H}_{t-1} \mathbf{W}_{ho} + \mathbf{b}_o)$$

**细胞状态**$\mathbf{C}_t$更新：

$$\mathbf{C}_t = \mathbf{F}_t \odot \mathbf{C}_{t-1} + \mathbf{I}_t \odot \tilde{\mathbf{C}}_t.$$


::right::


```python
# LSTM 的核心代码
def lstm(inputs, state, params):
    [W_xi, W_hi, b_i, W_xf, W_hf, b_f, 
     W_xo, W_ho, b_o, W_xc, W_hc, b_c,
     W_hq, b_q] = params
    (H, C) = state
    outputs = []
    for X in inputs:
        # @ 表示矩阵乘法，* 表示元素级乘法
        # 遗忘门
        F = torch.sigmoid((X @ W_xf) + (H @ W_hf) + b_f)
        #输入门
        I = torch.sigmoid((X @ W_xi) + (H @ W_hi) + b_i)
        # 输出门
        O = torch.sigmoid((X @ W_xo) + (H @ W_ho) + b_o)
        C_tilda = torch.tanh((X @ W_xc) + (H @ W_hc) + b_c)
        # 细胞状态更新
        C = F * C + I * C_tilda
        H = O * torch.tanh(C)
        Y = (H @ W_hq) + b_q
        outputs.append(Y)
    return torch.cat(outputs, dim=0), (H, C)
```

---
layout: default
---

# LSTM的简洁实现

<img src="/img/lstm/简洁实现.png" class="w-full rounded-xl shadow-2xl border border-gray-700" />


<!-- 使用高级API，我们可以直接实例化`LSTM`模型。高级API封装了前文介绍的所有配置细节。 

在这里要提到，LSTM只是一个基础模型，在实际工程中我们会在LSTM上面加入许多不同的算法或模型组件来提升性能

-->

---
src: ./lstmExample.md
---

---
layout: default
hide: true
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
