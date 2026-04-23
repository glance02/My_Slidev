---
name: magic-move
description: 通过平滑过渡在代码块之间展示代码变更动画
---

# Shiki Magic Move

使用平滑过渡展示代码变更动画（类似 Keynote 的 Magic Move）。

## 基础用法

`````md
````md magic-move
```js
console.log(`Step ${1}`)
```
```js
console.log(`Step ${1 + 1}`)
```
```ts
console.log(`Step ${3}` as string)
```
````
`````

注意：外层包裹块要使用 4 个反引号。

## 与行高亮配合

`````md
````md magic-move {at:4, lines: true}
```js {*|1|2-5}
let count = 1
function add() {
  count++
}
```

中间夹着的非代码块会被忽略。

```js {*}{lines: false}
let count = 1
const add = () => count += 1
```
````
`````

## 工作方式

- 把多个代码块包成一个整体
- 每个代码块就是一个“步骤”
- 点击时在各步骤之间做形态过渡
- 动画过程中依然保留语法高亮

## 资源

- Playground: https://shiki-magic-move.netlify.app/
