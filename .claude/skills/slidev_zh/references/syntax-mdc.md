---
name: comark
description: Comark 语法支持
---

# Comark 语法

增强版 Markdown，支持组件和样式语法。

## 启用

```md
---
comark: true
---
```

## 行内样式

```md
这是一段 [红色文字]{style="color:red"}
```

## 行内组件

```md
:inline-component{prop="value"}
```

## 图片属性

```md
![](/image.png){width=500px lazy}
```

## 块级组件

```md
::block-component{prop="value"}
这里是 **default** 插槽内容
::
```

## 使用场景

- 不写 HTML 也能添加行内样式
- 行内使用 Vue 组件
- 给图片添加属性
- 创建更复杂的组件布局

基于 Comark Syntax。
