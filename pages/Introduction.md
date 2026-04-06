---
layout: section
transition: slide-left
---

# Part 1
## 为什么需要智慧能源？

<!-- 从一个现实问题引入：电力是怎么"用不好"的？ -->


---
layout: default
---

# 能源系统正面临前所未有的挑战

<img src="/img/Intro/pic1.png" class="h-80 float-right mt-6 rounded-xl" />

### 三个核心矛盾

<v-clicks depth="1">

1. **可再生能源的间歇性**
   - 风能、光伏出力随天气剧烈波动
   - 2023年全球弃风弃光损失超过 **150 TWh**

2. **需求侧日趋复杂**
   - 电动汽车充电、数据中心用电急增
   - 用电峰谷差不断扩大

3. **实时决策窗口极短**
   - 电网频率偏差须在秒级内响应
   - 调度系统需同时处理海量传感器数据

</v-clicks>

<!-- 强调：不是为了用深度学习而用，而是问题本身驱动了技术选择 -->

---
layout: center
---

# 传统方法的乏力


<div class="grid grid-cols-3 gap-8 mt-10">

  <div class="flex gap-4 items-start">
    <div class="mt-1 w-4 h-4 rounded-full bg-sky-500 shrink-0 ring-4 ring-sky-500/20"></div>
    <div>
      <h3 class="font-bold text-base mb-2">线性假设</h3>
      <p class="text-sm leading-relaxed">
        ARIMA、回归模型以线性关系为根本前提。但负荷突变、可再生出力波动的本质是非线性过程——温度多升一度、云层多遮一秒，影响都不是线性叠加的。假设错了，精度的上限就已经注定。
      </p>
    </div>
  </div>

  <div class="flex gap-4 items-start">
    <div class="mt-1 w-4 h-4 rounded-full bg-violet-500 shrink-0 ring-4 ring-violet-500/20"></div>
    <div>
      <h3 class="font-bold text-base mb-2">人工规则</h3>
      <p class="text-sm leading-relaxed">
        EMS / SCADA 的调度逻辑依赖专家手工编写与维护。电网拓扑一变、分布式资源一增、新能源占比一高，规则就要重写。系统的复杂度在指数增长，人工规则的覆盖能力只能线性扩展。
      </p>
    </div>
  </div>

  <div class="flex gap-4 items-start">
    <div class="mt-1 w-4 h-4 rounded-full bg-emerald-500 shrink-0 ring-4 ring-emerald-500/20"></div>
    <div>
      <h3 class="font-bold text-base mb-2">时序建模</h3>
      <p class="text-sm leading-relaxed">
        SVM、随机森林将每个时间点当作独立样本处理，时序中的日周期、周周期、跨季节依赖完全无从捕捉。没有记忆，就没有对"过去"的感知，预测自然失准。
      </p>
    </div>
  </div>

</div>

<div class="mt-5 text-sm border-t border-slate-800 pt-5">

这三个缺陷指向同一个根本问题：**传统方法对数据的假设，已经跟不上能源系统的现实**。

</div>

<!--
这里总体提一下传统方法的不足之处

ARIMA 本质上属于线性时序模型

EMS 和 SCADA 是电网调度系统的两个工具

SVM ， Support Vector Machine（支持向量机），是一种经典的机器学习算法
-->

---
layout: default
---

# 深度学习的优势
 
<p class=" text-lg mt-1 mb-10">从感知数据，到理解时序，到驱动决策——形成完整的智能闭环</p>


<div class="relative mt-18">
 
<!-- 贯穿三列的连接线 -->
<div class="absolute top-8 left-[16.7%] right-[16.7%] h-px bg-gradient-to-r from-sky-500 via-violet-500 to-emerald-500 opacity-40"></div>
 
<div class="grid grid-cols-3 gap-0 text-left">
 
  <!-- 列 1 -->
  <div class="pr-10">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-sky-500 shrink-0 ring-4 ring-sky-500/20"></div>
      <span class="text-sky-400 text-xs tracking-widest uppercase font-semibold">感知 · 建模</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-2">捕捉时序规律</h3>
    <p class="text-sm leading-relaxed">
      能源数据天然是时间序列——负荷有日周期、周周期，也有难以预判的突变。深度学习能从原始数据中自动提取这些模式，无需人工设计特征，也无需对数据做线性假设。
    </p>
  </div>
 
  <!-- 列 2 -->
  <div class="px-10 border-x border-slate-700/60">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-violet-500 shrink-0 ring-4 ring-violet-500/20"></div>
      <span class="text-violet-400 text-xs tracking-widest uppercase font-semibold">预测 · 推断</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-2">量化不确定性</h3>
    <p class=" text-sm leading-relaxed">
      智慧能源的预测不能只给一个点估计——调度需要知道<span class="">误差有多大、极端情景有多可能</span>。深度学习可以输出概率分布与区间预测，让不确定性本身成为决策的输入。
    </p>
  </div>
 
  <!-- 列 3 -->
  <div class="pl-10">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-emerald-500 shrink-0 ring-4 ring-emerald-500/20"></div>
      <span class="text-emerald-400 text-xs tracking-widest uppercase font-semibold">优化 · 决策</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-2">驱动实时决策</h3>
    <p class=" text-sm leading-relaxed">
      预测的终点是决策。深度学习可以将预测结果与调度目标直接耦合，在<span class="">储能管理、需求响应、故障检测</span>等场景中替代静态规则，实现自适应的实时控制。
    </p>
  </div>
 
</div>
</div>
 
<div class="mt-10  text-sm border-t border-slate-800 pt-5">
  三个层次并非孤立模块——特征学习的质量决定预测上限，预测的不确定性直接塑造决策策略，构成<span class="">数据→预测→决策</span>的端到端智能链路。
</div>

<!-- 我们接下来主要介绍两个基础模型 -->
