---
name: monaco
description: 把代码块变成完整功能的编辑器
---

# Monaco 编辑器

把代码块变成完整功能的编辑器。

## 基础用法

````md
```ts {monaco}
console.log('HelloWorld')
```
````

## Diff 编辑器

对比两个代码版本：

````md
```ts {monaco-diff}
console.log('Original text')
~~~
console.log('Modified text')
```
````

## 编辑器高度

输入时自动增长：

````md
```ts {monaco} {height:'auto'}
console.log('Hello, World!')
```
````

固定高度：

````md
```ts {monaco} {height:'300px'}
// 这里是代码
```
````

## 配置

Monaco 编辑器的自定义选项见 `/custom/config-monaco`。
