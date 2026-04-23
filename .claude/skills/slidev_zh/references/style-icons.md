---
name: icons
description: 在幻灯片中使用开源图标
---

# 图标

可直接在 Markdown 中使用任意开源图标。底层由 unplugin-icons 和 Iconify 提供支持。

## 安装

```bash
pnpm add @iconify-json/[collection-name]
```

## 用法

使用组件语法 `<collection-icon-name />`：

```md
<mdi-account-circle />
<carbon-badge />
<uim-rocket />
<logos-vue />
```

## 常用图标集

- `@iconify-json/mdi` - Material Design Icons
- `@iconify-json/carbon` - Carbon Design
- `@iconify-json/logos` - SVG Logos
- `@iconify-json/twemoji` - Twitter Emoji

## 样式

和普通 HTML 元素一样写样式：

```html
<uim-rocket class="text-3xl text-red-400 mx-2" />
<uim-rocket class="text-3xl text-orange-400 animate-ping" />
```

## 浏览图标

- https://icones.js.org/
- https://icon-sets.iconify.design/
