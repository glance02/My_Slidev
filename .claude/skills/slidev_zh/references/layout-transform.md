---
name: transform-component
description: 使用 Transform 组件缩放元素且不影响幻灯片布局
---

# Transform 组件

缩放元素，同时不影响幻灯片布局。

## 用法

```md
<Transform :scale="0.5" origin="top center">
  <YourElements />
</Transform>
```

## Props

- `scale`：缩放比例（`0.5` = 50%，`2` = 200%）
- `origin`：变换原点（CSS `transform-origin` 的值）

## 使用场景

- 缩小较大的图表
- 缩放代码块
- 让超大内容适配页面
- 制造强调效果

## 相关功能

- 缩放所有幻灯片：在 headmatter 中使用 `canvasWidth` / `aspectRatio`
- 缩放单页幻灯片：使用 `zoom` frontmatter 选项
