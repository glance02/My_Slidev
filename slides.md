---
theme: '@ktym4a/slidev-theme-ktym4a'
layout: cover
themeConfig:
  baseColor: 'green' 
  colorPattern: 'rotation'
---

#  Hello, World!

欢迎来到我的 Slidev 演示文稿！这是一个使用 Bricks 主题的示例幻灯片。

<div class="flex flex-col items-center h-full text-left">

- 演讲者：[你的名字]
- 日期：[演讲日期]
- 信息收集：张三，李四，王五

</div>
---
layout: center
---

# RNN 的困境：梯度消失
序列越长，早期信息在反向传播时梯度指数级衰减，模型实际上"遗忘"了很久之前的信息。