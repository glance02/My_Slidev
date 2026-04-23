---
name: twoslash
description: 在代码块中以内联或悬浮方式显示 TypeScript 类型信息
---

# TwoSlash 集成

以内联或悬浮提示的方式显示 TypeScript 类型信息。

## 用法

````md
```ts twoslash
import { ref } from 'vue'

const count = ref(0)
//            ^?
```
````

## 功能

- 悬浮时显示类型信息
- 使用 `^?` 内联显示类型注解
- 展示错误和警告
- 完整接入 TypeScript 编译器

## 注解示例

```ts twoslash
const count = ref(0)
//            ^?
// 显示：const count: Ref<number>
```

## 使用场景

非常适合 TypeScript / JavaScript 教学材料，在展示类型时能帮助理解。

## 资源

- TwoSlash 文档：https://twoslash.netlify.app/
