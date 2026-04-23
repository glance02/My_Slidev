---
name: global-layers
description: 创建跨幻灯片持续存在的组件，例如页脚和背景
---

# 全局层

创建在多页幻灯片之间持续存在的组件。

## 层文件

在项目根目录创建：
- `global-top.vue` - 位于所有幻灯片之上（单实例）
- `global-bottom.vue` - 位于所有幻灯片之下（单实例）
- `slide-top.vue` - 位于每张幻灯片之上（每页一个实例）
- `slide-bottom.vue` - 位于每张幻灯片之下（每页一个实例）
- `custom-nav-controls.vue` - 自定义导航控件

## Z 轴顺序（从上到下）

1. `NavControls` / `custom-nav-controls.vue`
2. `global-top.vue`
3. `slide-top.vue`
4. 幻灯片内容
5. `slide-bottom.vue`
6. `global-bottom.vue`

## 示例：页脚

```html
<!-- global-bottom.vue -->
<template>
  <footer class="absolute bottom-0 left-0 right-0 p-2">Your Name</footer>
</template>
```

## 条件渲染

```html
<!-- 在 cover 布局中隐藏 -->
<template>
  <footer v-if="$nav.currentLayout !== 'cover'" class="absolute bottom-0 p-2">
    {{ $nav.currentPage }} / {{ $nav.total }}
  </footer>
</template>
```

## 导出说明

如果全局层依赖导航状态，请使用 `--per-slide` 导出选项。
