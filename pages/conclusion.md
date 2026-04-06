---
layout: section
transition: slide-left
---

# 总结

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

<!-- 细心的观众可能会发现，lstm是1997年的模型，这是将近30年前的模型，transformer是2017年的模型，也将近是20年前的模型。但是我举出的几个例子，却都是新近的在这些模型之上的研究成果。

-->