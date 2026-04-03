---
theme: dracula
title: 深度学习赋能智慧能源
info: |
  ## 深度学习与智慧能源
  探索 LSTM 与 Transformer 在智慧能源系统中的应用
highlighter: shiki
transition: slide-left
themeConfig:
  baseColor: 'green'
  colorPattern: 'single'
fonts:
  sans: SimSun
---

# 深度学习赋能智慧能源

### LSTM 与 Transformer 在智慧能源系统中的应用

<br>

- PPT演讲：雷显秋
- PPT制作：雷显秋、陈乙鑫
- 材料收集：闫星舟、缪佳成、史流阳、陈圣友

<div class="pt-6 text-gray-400">
  深度学习 · 智慧能源 · 时序预测
</div>



---
layout: two-cols
---

# 目录

<div class="mt-4 h-[360px] flex flex-col gap-4">
  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5 mr">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 01</div>
    <div class="font-semibold">为什么需要智慧能源？</div>
    <ul class="mt-2 text-sm text-gray-300 list-disc pl-5 space-y-1">
      <li>能源挑战背景</li>
      <li>传统方法的乏力</li>
      <li>深度学习的优势</li>
    </ul>
  </div>

  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5 mr">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 02</div>
    <div class="font-semibold">LSTM 与智慧能源</div>
    <ul class="mt-2 text-sm text-gray-300 list-disc pl-5 space-y-1">
      <li>LSTM 原理与实现</li>
      <li>电网负荷预测案例</li>
      <li>光伏微电网调度案例</li>
    </ul>
  </div>
</div>

::right::

<div class="h-[40px]" aria-hidden="true"></div>

<div class="mt-4 h-[360px] flex flex-col gap-4 mx">
  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 03</div>
    <div class="font-semibold">Transformer 与智慧能源</div>
    <ul class="mt-2 text-sm text-gray-300 list-disc pl-5 space-y-1">
      <li>自注意力机制与变体</li>
      <li>绿氢协同优化案例</li>
      <li>智能电网能耗预测案例</li>
    </ul>
  </div>

  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 04</div>
    <div class="font-semibold">总结与展望</div>
    <ul class="mt-2 text-sm text-gray-300 list-disc pl-5 space-y-1">
      <li>两种模型互补共存</li>
      <li>持续进化方向与未来趋势</li>
    </ul>
  </div>
</div>

---
src: ./pages/Introduction.md
---

---
src: ./pages/lstm.md
---

---
src: ./pages/transformer.md
---


---
layout: default
transition: slide-left
---

# 总结

<p class="text-slate-400 text-lg mt-1 mb-10">模型是工具，智慧能源才是目的</p>

<div class="relative">

<div class="absolute top-8 left-[50%] w-px h-36 bg-slate-700/60"></div>

<div class="grid grid-cols-2 gap-0 text-left">

  <!-- 左列 -->
  <div class="pr-14">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-sky-500 shrink-0 ring-4 ring-sky-500/20"></div>
      <span class="text-sky-400 text-xs tracking-widest uppercase font-semibold">互补 · 共存</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-3">两种范式，各有所长</h3>
    <p class="text-slate-400 text-sm leading-relaxed mb-3">
      LSTM 顺序处理时序、结构轻量，适合资源受限的<span class="text-slate-200">实时控制场景</span>；Transformer 通过注意力机制并行建模任意时间跨度的依赖，在<span class="text-slate-200">多变量、长序列、需要可解释性</span>的任务上更具优势。
    </p>
    <p class="text-slate-400 text-sm leading-relaxed">
      实际工程中两者并非替代关系，而是常常共存乃至融合——Aswan 案例中 LSTM 承担短期预测、优化算法执行调度；TFT 的门控结构本身也融合了类 LSTM 的序列编码机制。<span class="text-slate-300">这本身就是最好的例证。</span>
    </p>
  </div>

  <!-- 右列 -->
  <div class="pl-14">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-4 h-4 rounded-full bg-emerald-500 shrink-0 ring-4 ring-emerald-500/20"></div>
      <span class="text-emerald-400 text-xs tracking-widest uppercase font-semibold">进化 · 驱动</span>
    </div>
    <h3 class="text-white font-bold text-lg mb-3">模型在进化，需求也在进化</h3>
    <p class="text-slate-400 text-sm leading-relaxed mb-3">
      这两个模型之所以在能源领域有价值，根本原因在于它们都在回应同一个矛盾——<span class="text-slate-200">能源系统的不确定性在增加，而决策对精度的要求也在提高。</span>
    </p>
    <p class="text-slate-400 text-sm leading-relaxed">
      从 LSTM 到 Transformer，再到 Informer、PatchTST、iTransformer……每一次架构迭代，背后都是研究者在回应电网提出的真实问题。预测精度的每一个百分点，最终转化为<span class="text-slate-200">更少的弃光、更稳的电网、更低的碳排放。</span>
    </p>
  </div>

</div>
</div>

<div class="mt-10 text-slate-500 text-sm border-t border-slate-800 pt-5">
  深度学习与智慧能源的结合，不是一个已经完成的故事——<span class="text-slate-300">它仍在持续发生。</span>
</div>

---
layout: center
---

# 感谢聆听

<div class="mt-8 text-center text-lg text-gray-400">
欢迎提问与交流 💬
</div>
