---
theme: dracula
title: 深度学习赋能智慧能源
info: |
  ## 深度学习与智慧能源
  探索 LSTM 与 Transformer 在智慧能源系统中的应用
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: SimSun
---

# 深度学习赋能智慧能源

### LSTM 与 Transformer 在智慧能源系统中的应用

<div class="pt-6 text-gray-400">
  深度学习 · 智慧能源 · 时序预测
</div>
<!-- 开场白：能源是现代社会的血液，而如何让能源系统"更聪明"，正是我们今天要探讨的主题。 -->

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
      <li>深度学习的机遇</li>
    </ul>
  </div>

  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5 mr">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 02</div>
    <div class="font-semibold">LSTM 在智慧能源中的应用</div>
    <ul class="mt-2 text-sm text-gray-300 list-disc pl-5 space-y-1">
      <li>LSTM 原理回顾</li>
      <li>负荷预测案例</li>
    </ul>
  </div>
</div>

::right::

<div class="h-[40px]" aria-hidden="true"></div>

<div class="mt-4 h-[360px] flex flex-col gap-4 mx">
  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 03</div>
    <div class="font-semibold">Transformer 在智慧能源中的应用</div>
    <ul class="mt-2 text-sm text-gray-300 list-disc pl-5 space-y-1">
      <li>Attention 机制原理</li>
      <li>可再生能源预测</li>
    </ul>
  </div>

  <div class="flex-1 rounded-lg border border-gray-600/40 p-4 bg-white/5">
    <div class="text-xs tracking-wider uppercase text-gray-400 mb-1">Part 04</div>
    <div class="font-semibold">总结与展望</div>
    <div class="mt-2 text-sm text-gray-300">对比两种模型能力，并给出落地方向与未来趋势。</div>
  </div>
</div>

<!--
给听众一个清晰的路线图，让他们知道接下来15-20分钟的走向
-->

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
---

# 展望：深度学习 × 智慧能源的未来

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="text-center border rounded-lg p-4">
  <div class="text-3xl mb-2">🌱</div>
  <div class="font-bold mb-1">碳中和目标</div>
  <div class="text-sm text-gray-500">精准预测助力可再生能源并网，降低弃风弃光率</div>
</div>

<div class="text-center border rounded-lg p-4">
  <div class="text-3xl mb-2">🔋</div>
  <div class="font-bold mb-1">储能优化</div>
  <div class="text-sm text-gray-500">预测结合强化学习，实现电池充放电智能调度</div>
</div>

<div class="text-center border rounded-lg p-4">
  <div class="text-3xl mb-2">🤖</div>
  <div class="font-bold mb-1">大模型能源 AI</div>
  <div class="text-sm text-gray-500">基础模型迁移至能源领域，少样本高精度预测</div>
</div>

<div class="text-center border rounded-lg p-4">
  <div class="text-3xl mb-2">📡</div>
  <div class="font-bold mb-1">边缘智能</div>
  <div class="text-sm text-gray-500">轻量化模型部署于电表、传感器，实时本地推理</div>
</div>

<div class="text-center border rounded-lg p-4">
  <div class="text-3xl mb-2">🏙️</div>
  <div class="font-bold mb-1">虚拟电厂</div>
  <div class="text-sm text-gray-500">聚合分布式资源，AI 统一调度形成"虚拟大电厂"</div>
</div>

<div class="text-center border rounded-lg p-4">
  <div class="text-3xl mb-2">🔐</div>
  <div class="font-bold mb-1">安全与可解释性</div>
  <div class="text-sm text-gray-500">注意力可视化、对抗鲁棒性，推动模型可信部署</div>
</div>

</div>

<!-- 结尾：技术本身已经很成熟，接下来更多是落地和应用场景的创新 -->

---
layout: center
---

# 谢谢聆听

<div class="text-center mt-6 text-gray-400">

**核心信息回顾：**

> 能源数据本质是时序问题 → LSTM 捕捉短期规律 → Transformer 理解长程依赖  
> 两者协同，共同构建更聪明的能源系统

</div>

<div class="mt-8 text-center text-sm text-gray-400">
欢迎提问与交流 💬
</div>

<!-- 一句话总结：深度学习正在让能源系统从"被动应对"走向"主动预测"。 -->
