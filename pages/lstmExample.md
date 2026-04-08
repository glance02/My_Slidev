---
layout: section
transition: slide-left
---

# LSTM 案例一

---
layout: center
transition: slide-right
---
 
# 比利时国家电网负荷预测
 
<p class="text-slate-500 text-sm mt-0 mb-6">Dakheel & Çevik · <em>Energies</em> 2025, 18(11), 2842 · MDPI Open Access</p>
 
<div class="grid grid-cols-2 gap-10 items-start">
 
<div>
  <h3 class="text-sky-400 font-semibold text-base mb-3">背景与问题</h3>
  <p class="text-slate-300 text-sm leading-relaxed mb-5">
    比利时输电运营商 Elia 的电网负荷数据以 <strong class="text-white">15 分钟</strong>为粒度连续采集，全年超过 35,000 个时间点。数据呈现强烈的日内周期、周末效应与季节性漂移，且夹杂高频噪声——传统 ARIMA 在此类非平稳高频序列上误差持续偏高。
  </p>
  <h3 class="text-sky-400 font-semibold text-base mb-3">方法</h3>
  <p class="text-slate-300 text-sm leading-relaxed">
    以 LSTM 提取时序中的长短程依赖，再以 XGBoost 对残差进行二次修正，构成 <strong class="text-white">LSTM-XGBoost 混合框架</strong>。LSTM 负责捕捉连续时段内的趋势与波动，XGBoost 聚焦修正 LSTM 难以建模的非线性跳变残差。
  </p>
</div>
 
<div class="flex flex-col gap-3">
  <div class="rounded-xl overflow-hidden border border-slate-700/60 bg-slate-800/50">
    <img src="/img/lstm/case1.png" alt="Elia 电网预测值 vs 真实值" class="w-full object-cover" />
    <p class="text-slate-500 text-xs px-3 py-2">图：预测负荷（橙）与真实负荷（蓝）对比，来源 Fig. 2，Dakheel & Çevik 2025</p>
  </div>
</div>
 
</div>
 
---
layout: center
---

<img src="/img/lstm/case1_res.png" alt="残差对比" class="w-full rounded-xl border" />

<!-- 
截了一张论文的结果图，里面的数字部分是其他论文的结果，可以看出来lstm+XGBoost的结果明显优于其他方法。当然，要是不优于这篇论文也没法发出来
-->

---
layout: section
transition: slide-left
---

# LSTM 案例二

---
layout: center
---
 
# 埃及 Aswan 光伏微电网氢储能调度
 
<p class="text-slate-500 text-sm mt-0 mb-6">Hassan · <em>Scientific Reports</em> 2025, vol. 15, Art. 40394 · Nature Open Access</p>
 
<div class="grid grid-cols-2 gap-10 items-start">
 
<div>
  <h3 class="text-emerald-400 font-semibold text-base mb-3">背景与问题</h3>
  <p class="text-slate-300 text-sm leading-relaxed mb-5">
    埃及 Aswan 是全球太阳辐照度最高的地区之一，5 kW 光伏阵列接入含氢储能系统的智能微电网。核心挑战是：光伏出力高度随机，而氢储能的充放电调度需要提前预判出力曲线，否则将产生大量弃电或过度依赖电网购电。
  </p>
  <h3 class="text-emerald-400 font-semibold text-base mb-3">方法</h3>
  <p class="text-slate-300 text-sm leading-relaxed">
    LSTM 对 15 分钟粒度的光伏出力与负荷数据进行短期预测，预测结果作为 <strong class="text-white">Krill Herd 优化算法（KHA）</strong>的输入，生成每个调度周期的最优充放电策略，每次决策耗时不足 2 秒。
  </p>
</div>
 
<div class="flex flex-col gap-3">
  <div class="rounded-xl overflow-hidden border border-slate-700/60 bg-slate-800/50">
    <img src="/img/lstm/case2.png" alt="Aswan 调度结果对比" class="w-full object-cover" />
    <p class="text-slate-500 text-xs px-3 py-2">图：30 天电网购电量与弃光量改善对比，来源 Fig. 8，Hassan 2025</p>
  </div>
</div>
 
</div>

<!-- 
grid import 是电网购电量的意思。

Krill Herd Algorithm（KHA）是 2012 年由 Gandomi 和 Alavi 提出的一种群体智能优化算法，灵感来自南极磷虾（krill）的群体行为。 
-->
 
---
layout: center
hide: true
---
 
# 案例二：结果与意义
 
<p class="text-slate-500 text-sm mt-0 mb-8">埃及 Aswan 光伏微电网 · 15 分钟分辨率 · 30 天仿真验证</p>
 
<div class="grid grid-cols-4 gap-5 mb-8">
  <div class="text-center">
    <div class="text-3xl font-black text-emerald-400 mb-1">4.8<span class="text-xl">%</span></div>
    <div class="text-slate-400 text-sm">MAPE</div>
    <div class="text-slate-600 text-xs mt-1">预测精度</div>
  </div>
  <div class="text-center">
    <div class="text-3xl font-black text-emerald-400 mb-1">−35.6<span class="text-xl">%</span></div>
    <div class="text-slate-400 text-sm">电网购电</div>
    <div class="text-slate-600 text-xs mt-1">1295W → 834W</div>
  </div>
  <div class="text-center">
    <div class="text-3xl font-black text-emerald-400 mb-1">−21.4<span class="text-xl">%</span></div>
    <div class="text-slate-400 text-sm">弃光量</div>
    <div class="text-slate-600 text-xs mt-1">光伏利用率提升</div>
  </div>
  <div class="text-center">
    <div class="text-3xl font-black text-emerald-400 mb-1">7.76<span class="text-xl">kg</span></div>
    <div class="text-slate-400 text-sm">日均减排</div>
    <div class="text-slate-600 text-xs mt-1">CO₂ 当量</div>
  </div>
</div>
 
<div class="border-t border-slate-800 pt-6 grid grid-cols-2 gap-8">
  <div>
    <h4 class="text-slate-300 font-semibold text-sm mb-2">LSTM 在其中的角色</h4>
    <p class="text-slate-400 text-sm leading-relaxed">LSTM 提供的短期预测质量直接决定了优化器的决策上限。当预测 MAPE 从 8% 降至 4.8% 时，弃光减少量几乎同比提升——预测精度与调度收益呈强正相关。</p>
  </div>
  <div>
    <h4 class="text-slate-300 font-semibold text-sm mb-2">从案例到一般结论</h4>
    <p class="text-slate-400 text-sm leading-relaxed">这一"预测驱动调度"的范式具有可移植性：只要存在时序出力数据与可控储能资源，LSTM + 优化算法的组合逻辑即可适配风电、储热等其他场景。</p>
  </div>
</div>