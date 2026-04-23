---
name: syntax
description: Slidev 演示文稿的核心 Markdown 语法
---

# Slidev Markdown 语法

Slidev 演示文稿的核心 Markdown 语法。

## 幻灯片分隔符

使用前后留空行的 `---`：

```md
# 幻灯片 1

内容

---

# 幻灯片 2

更多内容
```

## Headmatter（整套配置）

第一段 frontmatter 用于配置整套演示文稿：

```md
---
theme: default
title: 我的演示文稿
lineNumbers: true
---

# 第一页
```

## 单页 Frontmatter

每一页幻灯片都可以有自己的 frontmatter：

```md
---
layout: center
background: /image.jpg
class: text-white
---

# 居中页
```

## 演讲者备注

放在幻灯片结尾的 HTML 注释会变成演讲者备注：

```md
# 我的幻灯片

这里是内容

<!--
这些是演讲者备注。
- 记得提到 X
- 演示这个功能
-->
```

## 代码块

标准 Markdown 代码块，使用 Shiki 高亮：

````md
```ts
const hello = 'world'
```
````

配合功能：
````md
```ts {2,3}              // 行高亮
```ts {1|2-3|all}        // 基于点击的高亮
```ts {monaco}           // Monaco 编辑器
```ts {monaco-run}       // 可运行代码
```ts twoslash           // TypeScript 类型
```
````

## LaTeX 数学公式

行内：`$E = mc^2$`

块级：
```md
$$
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

## 图表

Mermaid：
````md
```mermaid
graph LR
  A --> B --> C
```
````

PlantUML：
````md
```plantuml
@startuml
Alice -> Bob : Hello
@enduml
```
````

## Comark 语法

通过 `comark: true` 启用：

```md
[带样式的文本]{style="color:red"}
![](/image.png){width=500px}
::component{prop="value"}
```

## 作用域 CSS

样式只会应用到当前幻灯片：

```md
# 红色标题

<style>
h1 { color: red; }
</style>
```

## 导入幻灯片

```md
---
src: ./pages/intro.md
---
```

导入指定页：
```md
---
src: ./other.md#2,5-7
---
```
