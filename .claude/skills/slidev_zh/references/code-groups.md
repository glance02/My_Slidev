---
name: code-groups
description: 通过标签页和自动图标把多个代码块分组展示
---

# 代码分组

使用标签页和自动图标把多个代码块分组展示。

## 要求

在 headmatter 中启用 Comark 语法：

```md
---
comark: true
---
```

## 语法

````md
::code-group

```sh [npm]
npm i @slidev/cli
```

```sh [yarn]
yarn add @slidev/cli
```

```sh [pnpm]
pnpm add @slidev/cli
```

::
````

## 标题图标匹配

图标会根据标题名称自动匹配。若要启用内置图标，请安装 `@iconify-json/vscode-icons`。

支持：npm、yarn、pnpm、bun、deno、vue、react、typescript、javascript 等等。

## 自定义图标

在标题中使用 `~icon~` 语法：

````md
```js [npm ~i-uil:github~]
console.log('Hello!')
```
````

需要：
1. 安装图标集合：`pnpm add @iconify-json/uil`
2. 在 `uno.config.ts` 中加入 safelist：

```ts
export default defineConfig({
  safelist: ['i-uil:github']
})
```
