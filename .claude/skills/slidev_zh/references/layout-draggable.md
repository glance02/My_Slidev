---
name: draggable-elements
description: 在演示过程中通过拖拽移动、缩放和旋转元素
---

# 可拖拽元素

在演示过程中通过拖拽移动、缩放和旋转元素。

## 指令用法

### 使用 Frontmatter 中的位置

```md
---
dragPos:
  square: Left,Top,Width,Height,Rotate
---

<img v-drag="'square'" src="https://sli.dev/logo.png">
```

### 内联位置

```md
<img v-drag="[Left,Top,Width,Height,Rotate]" src="https://sli.dev/logo.png">
```

## 组件用法

```md
---
dragPos:
  foo: Left,Top,Width,Height,Rotate
---

<v-drag pos="foo" text-3xl>
  可拖拽内容
</v-drag>
```

## 可拖拽箭头

```md
<v-drag-arrow />
```

## 控制方式

- 双击：开始拖拽
- 方向键：移动元素
- Shift + 拖拽：保持宽高比
- 点击外部：停止拖拽

## 自动高度

把 Height 设为 `NaN` 或 `_`，即可根据内容自动计算高度。
