---
layout: section
---

# Part 3
## Transformer 与智慧能源

<!-- Transformer：用"注意力"替代"记忆"，一次看全整段序列 -->
---
layout: two-cols
class: my-auto
---

# Transformer 的核心：自注意力机制

Transformer 来自 2017 年 Google 的论文  
**"Attention is All You Need"**（Vaswani et al.）

**核心思想**：序列中的每个位置，都能直接"关注"到其他任意位置，无需逐步传递。

**自注意力计算**：

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

- $Q$（Query）：当前位置"想要什么"
- $K$（Key）：其他位置"提供什么"
- $V$（Value）：实际携带的信息

::right::

<img src="./../img/Transformer.png" class="h-95 mx-20 mt-15 rounded-2xl" />

---
layout: two-cols
class: my-auto
---

# Transformer直观理解

<v-clicks>

想象你是一个大型园区的能源管理者，面前有这些资产需要调度：

- 🏢 **几十栋楼宇** — 空调怎么调？能耗怎么控？
- ☀️ **一座光伏电站** — 今天的发电量怎么预测？
- 🔋 **两座储能站** — 什么时候充放电？容量如何分配？
- ⚡ **一排充电桩** — 要不要限制功率？

</v-clicks>

::right::

<img src="./../img/园区能源.png" class="h-95 mt-15 rounded-xl" />

---
layout: two-cols
class: my-auto
---

# 传统方法

<v-clicks>

把不同决策分开来做：

- 📊 **负荷预测**（模型 A）— 查看历史用电数据
- ☀️ **光伏预测**（模型 B）— 查看天气预报
- 🔋 **储能优化**（模型 C）— 查看电池状态

</v-clicks>

<v-click>

**最后人工协调** → **效率低且容易出错**

> 就像请了三个不同的专家，各看各的数据，最后开会商量

</v-click>

::right::

<v-click>

# Transformer



**一张”大表格”汇聚所有数据**：过去一个月的负荷、未来三天的天气预报、每辆车的充电习惯、储能电池的健康状态……

</v-click>

<v-click>

**自注意力机制自动发现关联**

- 🏢↔🏢 空调负荷与隔壁楼办公人数强相关
- 🔋→⚡ 下午三点前留出容量，因为四点有充电高峰

</v-click>

<v-click>

Transformer提供“全局感知的预测或状态表示”，再用于优化或决策

</v-click>



---
layout: statement
---

# “互相感知”

Transformer 在能源领域最朴素的价值：

不是做一个更准的预测，

而是让所有的预测和决策能够**互相感知**。

---
layout: default
---

<div class="aspect-video rounded-xl shadow-2xl overflow-hidden border border-gray-700 mb-100 ">
  <iframe
    src="//player.bilibili.com/player.html?isOutside=true&aid=586825595&bvid=BV1Zz4y127h1&cid=302259616&p=1"
    allowfullscreen="true"
    class="w-full h-full"
  ></iframe>
</div>



---
layout: section
---

# Transformer 案例

---
layout: two-cols
class: my-auto
---

# 绿氢背后的“调度大脑”

[内蒙古多伦，大唐集团煤化工基地](https://sklict.zju.edu.cn/2025/0724/c85586a3071334/page.htm)

<v-clicks depth="2">

- 传统：煤制氢，碳排放强度高
- 改变：周边光、风资源丰富 → **绿电制绿氢**
- 挑战：风电和光伏天然具有波动性，而电解槽的连续运行和化工厂的稳定用氢需求之间存在刚性约束
  - 频繁制氢 → 设备寿命缩短
  - 保守运行 → 绿氢替代率低

</v-clicks>

::right::

<img src="./../img/大唐多伦化工厂.png" class="h-70 rounded-xl mx-auto mt-10" />

---
layout: two-cols
---

<img src="./../img/大唐中控技术.png" class="h-100 rounded-xl mt-10" />

::right::

## Transformer多能源协同优化模型

<v-clicks>

**多路数据输入**：气象预报 / 风光出力 / 用氢需求 / 电解槽状态

**核心机制**：Self-Attention机制学习风光资源与生产负荷在不同时间尺度下的耦合关系，同时在设备启停、储氢罐容量、电网交互等工业约束下，滚动生成优化的 24 小时调度指令

</v-clicks>

<v-click>

### 结果：绿氢占比 **29.54% → 54.3%**

| 指标 | 数值 |
|------|------|
| 可再生能源替代率 | **87.5%** |
| 年减碳 | **42 万吨** |

</v-click>

--- 
layout: default
---

