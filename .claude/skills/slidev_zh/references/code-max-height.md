---
name: max-height
description: 为代码块设置固定高度，并在代码较长时启用滚动
---

# 代码块最大高度

为代码块设置固定高度，并在内容过长时滚动显示。

## 用法

````md
```ts {2|3|7|12}{maxHeight:'100px'}
function add(
  a: Ref<number> | number,
  b: Ref<number> | number
) {
  return computed(() => unref(a) + unref(b))
}
/// ...想写多少行都可以
const c = add(1, 2)
```
````

## 配合行高亮占位符

如果只需要 `maxHeight`，可以使用 `{*}`：

````md
```ts {*}{maxHeight:'100px'}
// 这里是长代码
```
````

## 使用场景

当代码太长，一页放不下，但你又想通过滚动完整展示时非常适合。
