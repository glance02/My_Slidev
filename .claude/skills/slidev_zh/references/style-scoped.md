---
name: scoped
description: 幻灯片作用域 CSS 样式
---

# 幻灯片作用域样式

定义只作用于当前幻灯片的 CSS。

## 用法

```md
# 这是红色标题

<style>
h1 {
  color: red;
}
</style>

---

# 其他幻灯片不会受影响
```

## 默认就是 Scoped

幻灯片中的所有 `<style>` 标签都会自动加作用域。

由于作用域机制，子组合器（`.a > .b`）的效果可能不如预期。

## 配合 UnoCSS 的嵌套 CSS

```md
# Slidev

> Hello **world**

<style>
blockquote {
  strong {
    --uno: 'text-teal-500 dark:text-teal-400';
  }
}
</style>
```

## 全局样式

如果要写全局样式，请使用项目中的 `styles/index.css`。
