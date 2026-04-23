---
name: line-numbers
description: 为代码块全局或按块启用行号
---

# 代码块行号

为代码块启用行号。

## 全局设置

在 headmatter 中为所有代码块启用：

```md
---
lineNumbers: true
---
```

## 单个代码块设置

````md
```ts {6,7}{lines:true,startLine:5}
function add(
  a: Ref<number> | number,
  b: Ref<number> | number
) {
  return computed(() => unref(a) + unref(b))
}
```
````

## 选项

- `lines: true/false` - 启用 / 禁用行号
- `startLine: number` - 起始行号（默认：`1`）

## 与行高亮配合使用

与其他功能组合时，可使用 `{*}` 作为占位符：

````md
```ts {*}{lines:true,startLine:5}
// 这里是代码
```
````
