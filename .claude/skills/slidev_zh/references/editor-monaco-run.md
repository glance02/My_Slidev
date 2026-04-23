---
name: monaco-run
description: 直接在编辑器中运行代码并查看结果
---

# Monaco Runner

直接在编辑器中运行代码并查看结果。

## 基础用法

````md
```ts {monaco-run}
function distance(x: number, y: number) {
  return Math.sqrt(x ** 2 + y ** 2)
}
console.log(distance(3, 4))
```
````

会显示一个“Run”按钮，并在代码下方展示输出结果。

## 禁用自动运行

````md
```ts {monaco-run} {autorun:false}
console.log('点击播放按钮再运行我')
```
````

## 点击后显示输出

````md
```ts {monaco-run} {showOutputAt:'+1'}
console.log('1 次点击后显示')
```
````

## 支持的语言

- JavaScript
- TypeScript

如果需要其他语言，可在 `/custom/config-code-runners` 中配置自定义代码运行器。
