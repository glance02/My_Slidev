---
name: line-highlighting
description: 在代码块中高亮指定行，支持静态高亮和基于点击的动态高亮
---

# 行高亮

高亮代码块中的指定行。

## 静态高亮

````md
```ts {2,3}
function add(
  a: Ref<number> | number,
  b: Ref<number> | number
) {
  return computed(() => unref(a) + unref(b))
}
```
````

## 动态高亮（基于点击）

使用 `|` 分隔不同阶段：

````md
```ts {2-3|5|all}
function add(
  a: Ref<number> | number,
  b: Ref<number> | number
) {
  return computed(() => unref(a) + unref(b))
}
```
````

点击流程：第 2-3 行 -> 第 5 行 -> 全部行。

## 特殊值

- `hide` - 隐藏代码块
- `none` - 显示代码但不高亮
- `all` - 高亮全部行

````md
```ts {hide|none|all}
// 隐藏 -> 无高亮 -> 全部高亮
```
````
