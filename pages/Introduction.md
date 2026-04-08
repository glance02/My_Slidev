---
layout: section
transition: slide-left
---

# Part 1
## 深度学习与智慧能源

<!-- 从一个现实问题引入：电力是怎么"用不好"的？ -->


---
layout: default
---

<div class="h-full flex flex-col justify-center">

# 能源系统正面临的一些挑战

<div class="mx-auto mt-6 flex w-fit items-start gap-10">
  <div class="max-w-2xl">


  1. **可再生能源波动性**：<br>&emsp;风电、光伏受天气影响，出力间歇性强、随机性大
  2. **供需实时平衡**：<br>&emsp;源荷双侧不确定性加剧，电网稳定性受威胁
  3. **多源异构数据**：<br>&emsp;物联网设备激增，数据协议不统一、质量参差不齐	
  4. **系统复杂性**：<br>&emsp;分布式能源、储能、负荷多元互动，耦合关系复杂
  5. **预测精度需求**：<br>&emsp;新能源预测误差直接影响电网安全与经济性

  </div>

  <img src="/img/Intro/pic1.png" class="h-80 rounded-xl" />
</div>
</div>

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
        ARIMA、回归模型以线性关系为根本前提。但负荷突变、可再生出力波动的本质是非线性过程——温度多升一度、云层多遮一秒，影响都不是线性叠加的。
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
        SVM、随机森林将每个时间点当作独立样本处理，时序中的日周期、周周期、跨季节依赖完全无从捕捉。没有记忆，就没有对"过去"的感知。
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
layout: center
---

# 深度学习的优势

<div class="relative mt-18">
 
<!-- 贯穿三列的连接线 -->
<div class="absolute top-8 left-[16.7%] right-[16.7%] h-px bg-gradient-to-r from-sky-500 via-violet-500 to-emerald-500 opacity-40"></div>
 
<div class="grid grid-cols-3 gap-0 text-left">
 
  <!-- 列 1 -->
  <div class="pr-10">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-sky-500 shrink-0 ring-4 ring-sky-500/20"></div>
      <span class="text-sky-400 text-xs tracking-widest uppercase font-semibold">非线性</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-2">处理非线性关系</h3>
    <p class="text-sm leading-relaxed">
      深度学习模型在处理高维数据集时，能够自动提取有意义的特征，这使得它们比传统机器学习技术更适合可再生能源预测
    </p>
  </div>
 
  <!-- 列 2 -->
  <div class="px-10 border-x border-slate-700/60">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-violet-500 shrink-0 ring-4 ring-violet-500/20"></div>
      <span class="text-violet-400 text-xs tracking-widest uppercase font-semibold">动态优化</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-2">实时自适应</h3>
    <p class=" text-sm leading-relaxed">
      深度学习框架能够实时处理物联网传感器数据、动态调整能源分配策略等
    </p>
  </div>
 
  <!-- 列 3 -->
  <div class="pl-10">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-emerald-500 shrink-0 ring-4 ring-emerald-500/20"></div>
      <span class="text-emerald-400 text-xs tracking-widest uppercase font-semibold">时序</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-2">捕捉时序规律</h3>
    <p class=" text-sm leading-relaxed">
      能源数据天然是时间序列，深度学习能从原始数据中自动提取这些模式，无需人工设计特征，也无需对数据做线性假设
    </p>
  </div>
 
</div>
</div>
 
<div class="mt-10  text-sm border-t border-slate-800 pt-5">
  从非线性建模，到实时自适应，再到时序规律捕捉，深度学习为智慧能源提供了一条从数据理解到决策优化的完整路径
</div>

<!-- 
依次对应前面提出的三个传统方法的问题

我们接下来主要介绍两个基础模型 
-->
