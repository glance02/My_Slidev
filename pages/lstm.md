---
layout: section
transition: slide-left
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
为了解决这个问题，LSTM诞生了
-->


---
layout: center
---

# LSTM直觉解释

LSTM的设计或多或少的借鉴了人类对于自然语言处理的直觉性经验

<div class="grid grid-cols-2 gap-6 mt-7">

<div class="bg-gradient-to-br from-blue-500/10 to-blue-500/5 border border-blue-500/20 rounded-lg p-6">
  <div class="flex items-center gap-3 mb-3">
    <h3 class="text-lg font-bold text-blue-400">① 信息优先级</h3>
  </div>
  <p class="text-slate-300 text-sm leading-relaxed">
    在一个时间序列中，<span class="text-blue-200 font-semibold">不是所有信息都是同等有效的</span>。大多数情况下，存在 <span class="text-blue-200">"关键词"或"关键帧"</span>。
  </p>
</div>

<div class="bg-gradient-to-br from-violet-500/10 to-violet-500/5 border border-violet-500/20 rounded-lg p-6">
  <div class="flex items-center gap-3 mb-3">
    <h3 class="text-lg font-bold text-violet-400">② 动态概括</h3>
  </div>
  <p class="text-slate-300 text-sm leading-relaxed">
    我们在从头到尾阅读时<span class="text-violet-200 font-semibold">自动概括</span>已阅内容，<span class="text-violet-200">用之前的理解帮助解析后文</span>——这是一个持续的选择性记忆过程。
  </p>
</div>

</div>

<br>

基于以上这两点，LSTM的设计者提出了“长短期记忆”的概念：

**只有一部分的信息需要长期的记忆，而有的信息可以不记下来**。


<!-- 直觉性经验也就是片段概括的流程。人类一般都会先总结出关键词，然后再根据关键词进行重述 -->
---
layout: default
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

# LSTM的代码实现

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

<!-- lstm是一个比较简单的模型，在与能源领域结合的时候，往往是作为基础组件使用，和不同的模块或方法进行组合 -->

---
layout: default
hide: true
---

# LSTM的简洁实现

<img src="/img/lstm/简洁实现.png" class="w-full rounded-xl shadow-2xl border border-gray-700" />


<!-- 

由于我比较懒，没有去排版代码和图片，就直接截了一张图片来展示简洁的实现。

使用高级API，我们可以直接实例化`LSTM`模型。高级API封装了前文介绍的所有配置细节。 

在这里要提到，LSTM只是一个基础模型，在实际工程中我们会在LSTM上面加入许多不同的算法或模型组件来提升性能

-->

---
src: ./lstmExample.md
---
