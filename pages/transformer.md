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

# Transformer直观理解

<v-clicks>

想象你是一个大型园区的能源管理者，面前有这些资产需要调度：

- 🏢 **几十栋楼宇** — 空调怎么调？能耗怎么控？
- ☀️ **一座光伏电站** — 今天的发电量怎么预测？
- 🔋 **两座储能站** — 什么时候充放电？容量如何分配？
- ⚡ **一排充电桩** — 要不要限制功率？

</v-clicks>

::right::

<img src="/img/transformer/园区能源.png" class="h-95 mt-15 rounded-xl" />

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

**最后人工协调** 

> 就像请了三个不同的专家，各看各的数据，最后开会商量

</v-click>

::right::

<v-click>

# Transformer



**一张”大表格”汇聚所有数据**：过去一个月的负荷、未来三天的天气预报、每辆车的充电习惯、储能电池的健康状态……

</v-click>

<v-click>

**自注意力机制自动发现关联**

- 空调负荷与隔壁楼办公人数强相关
- 下午三点前留出容量，因为四点有充电高峰

</v-click>

<v-click>

Transformer提供“全局感知的预测或状态表示”，再用于优化或决策

</v-click>


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

<img src="/img/transformer/Transformer.png" class="h-95 mx-20 mt-15 rounded-2xl" />

---
layout: default
hide: true
---

<div class="aspect-video rounded-xl shadow-2xl overflow-hidden border border-gray-700 mb-100 ">
  <iframe
    src="//player.bilibili.com/player.html?isOutside=true&aid=586825595&bvid=BV1Zz4y127h1&cid=302259616&p=1"
    allowfullscreen="true"
    class="w-full h-full"
  ></iframe>
</div>

---
layout: default
---

# 面向能源时序的 Transformer 变体

<p class="text-slate-400 text-lg mt-1 mb-8">原始 Transformer 直接用于能源预测效果有限——研究者针对时序数据的特点对其进行了系统性改造</p>

<div class="grid grid-cols-2 gap-x-10 gap-y-5">

  <!-- Informer -->
  <div class="flex gap-4 items-start">
    <div class="mt-1 w-2 h-2 rounded-full bg-sky-400 shrink-0 ring-2 ring-sky-400/30 mt-2"></div>
    <div>
      <div class="flex items-baseline gap-2 mb-1">
        <span class="text-sky-400 font-bold text-base">Informer</span>
        <span class="text-slate-600 text-xs">Zhou et al., 2021 · AAAI Best Paper</span>
      </div>
      <p class="text-slate-400 text-sm leading-relaxed">
        原始 Transformer 的注意力计算复杂度为 O(L²)，序列一长就慢得无法用于实际电网。Informer 引入 <span class="text-slate-200">ProbSparse 稀疏注意力</span>，只保留得分最高的 Top-k 注意力对，将复杂度降至 O(L log L)，使长序列（如一年 15 分钟粒度）的多步预测成为可能。常用于日前至周前的负荷与可再生出力预测。
      </p>
    </div>
  </div>

  <!-- TFT -->
  <div class="flex gap-4 items-start">
    <div class="mt-1 w-2 h-2 rounded-full bg-rose-400 shrink-0 ring-2 ring-rose-400/30 mt-2"></div>
    <div>
      <div class="flex items-baseline gap-2 mb-1">
        <span class="text-rose-400 font-bold text-base">TFT</span>
        <span class="text-slate-600 text-xs">Temporal Fusion Transformer · Lim et al., 2021 · IJF</span>
      </div>
      <p class="text-slate-400 text-sm leading-relaxed">
        专为工程落地设计：门控机制过滤无关输入，变量选择网络自动识别重要特征，注意力权重提供<span class="text-slate-200">可解释的时间步重要性输出</span>，可直接告知调度员"模型在关注哪个时段"。同时原生支持已知未来协变量（如节假日、计划检修）的输入，在工业能源管理系统（EMS）中已有真实部署案例。
      </p>
    </div>
  </div>

  <!-- iTransformer -->
  <div class="flex gap-4 items-start">
    <div class="mt-1 w-2 h-2 rounded-full bg-amber-400 shrink-0 ring-2 ring-amber-400/30 mt-2"></div>
    <div>
      <div class="flex items-baseline gap-2 mb-1">
        <span class="text-amber-400 font-bold text-base">iTransformer</span>
        <span class="text-slate-600 text-xs">Liu et al., 2024 · ICLR</span>
      </div>
      <p class="text-slate-400 text-sm leading-relaxed">
        提出"倒置"视角：将每个<span class="text-slate-200">变量（而非时间步）作为 token</span>，注意力机制因此建模的是变量之间的相关性（如温度与负荷、风速与出力之间的耦合），而前馈网络则负责编码各变量自身的时序表示。在引入多气象变量的电网预测中，其精度提升效率比 PatchTST 高出 3 倍。
      </p>
    </div>
  </div>

  <!-- FEDformer -->
  <div class="flex gap-4 items-start">
    <div class="mt-1 w-2 h-2 rounded-full bg-cyan-400 shrink-0 ring-2 ring-cyan-400/30 mt-2"></div>
    <div>
      <div class="flex items-baseline gap-2 mb-1">
        <span class="text-cyan-400 font-bold text-base">FEDformer</span>
        <span class="text-slate-600 text-xs">Zhou et al., 2022 · ICML</span>
      </div>
      <p class="text-slate-400 text-sm leading-relaxed">
        将注意力计算从时域迁移至<span class="text-slate-200">频域（傅里叶变换）</span>，在频率空间中直接识别负荷或出力的主导周期成分，再做稀疏选择。这一设计使模型对能源数据中的周期性噪声天然鲁棒，在单变量预测任务上比 Autoformer 精度提升超过 22%，且计算效率更高。
      </p>
    </div>
  </div>

</div>

---
layout: section
---

# Transformer 案例一

---
layout: two-cols
class: my-auto
---

# 绿氢背后的“调度大脑”

[内蒙古多伦，大唐集团煤化工基地](https://sklict.zju.edu.cn/2025/0724/c85586a3071334/page.htm)

<v-clicks depth="1">

- 传统：煤制氢，碳排放强度高
- 优势：周边光、风资源丰富 → **绿电制绿氢**
- 挑战：风电和光伏天然具有波动性，而电解槽的连续运行和化工厂的稳定用氢需求之间存在刚性约束
  - 频繁制氢 → 设备寿命缩短
  - 保守运行 → 绿氢替代率低

</v-clicks>

::right::

<img src="/img/transformer/大唐多伦化工厂.png" class="h-70 rounded-xl mx-auto mt-10 ml-8" />


<!--这是一则来自 2025-06-30 的新闻 -->

---
layout: two-cols
class: my-auto
---

<img src="/img/transformer/大唐中控技术.png" class="h-110 rounded-xl mt-5" />

::right::

## 时间序列大模型TPT

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
layout: section
---

# Transformer 案例二

---
layout: center
transition: slide-right
---

# 智能电网能耗预测中的 Temporal Fusion Transformer

<p class="text-slate-500 text-sm mt-0 mb-6">Badhe et al. · <em>Frontiers in Artificial Intelligence</em> 2025, 8:1542320 · CC BY Open Access</p>

<div class="grid grid-cols-2 gap-10 items-start">

<div>
  <h3 class="text-violet-400 font-semibold text-base mb-3">背景与问题</h3>
  <p class="text-slate-300 text-sm leading-relaxed mb-5">
    智能电网中的能耗数据受<strong class="text-white">建筑类型、天气条件、时段负荷</strong>等多重因素交叉影响，呈现出强非线性与跨尺度的时序结构。传统 LSTM 对这类多变量、多时间尺度的依赖关系建模能力有限，预测精度存在明显瓶颈。研究采用来自 UCI Household 数据集的真实家庭用电记录作为实验基准。
  </p>
  <h3 class="text-violet-400 font-semibold text-base mb-3">方法</h3>
  <p class="text-slate-300 text-sm leading-relaxed">
    以 <strong class="text-white">Temporal Fusion Transformer（TFT）</strong>为核心预测模型——其自注意力机制同时建模短期波动与长期趋势，门控机制过滤无关输入，并保留对各时间步特征重要性的可解释输出。在此之上，引入 <strong class="text-white">Aquila Optimizer（AO）</strong>对学习率、注意力头数等关键超参数进行自动调优，显著加速收敛。
  </p>
</div>

<div>
  <div class="rounded-xl overflow-hidden border border-slate-700/60 bg-slate-800/50">
    <FullscreenImg src="/img/transformer/case2.png" alt="各模型 RMSE 对比" class="w-full object-cover" />
    <p class="text-slate-500 text-xs px-3 py-2">图：各方法 RMSE 对比（AO-TFT 最低）</p>
  </div>
  <p class="text-slate-600 text-xs mt-3 leading-relaxed">
    与 SVM、ANN、CNN-1D、LSTM、Bi-LSTM、CNN-LSTM 及未调优 TFT 的横向对比，AO-TFT 在所有指标上均取得最优。
  </p>
</div>

</div>

<!-- SVM是支持向量机（Support Vector Machine），ANN是人工神经网络（Artificial Neural Network）
CNN-1D是一维卷积神经网络（1D Convolutional Neural Network），Bi-LSTM 是向长短期记忆网络（Bidirectional LSTM）
CNN-LSTM — 卷积与长短期记忆的混合网络
 -->

---
layout: center
---

## TABLE: Comparison of different methods based on MAE and RMSE (with 95% confidence intervals).

<img src="\img\transformer\case2_res.png" class="w-full rounded-xl border">

<!-- 
confidence intervals 是置信度的意思

这张图和之前的那张图的结果其实差不多，这个列表把RMSE和MAE两个参数都列出来了
 -->