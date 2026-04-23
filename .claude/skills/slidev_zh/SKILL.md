---
name: slidev
description: 使用 Slidev 结合 Markdown、Vue 组件、代码高亮、动画与交互能力，为开发者创建和演示基于 Web 的幻灯片。适用于技术演讲、会议分享、代码讲解、教学材料或开发者演示文稿。
---

# Slidev - 面向开发者的演示幻灯片

基于 Vite、Vue 和 Markdown 的 Web 幻灯片制作工具。

## 适用场景

- 带实时代码示例的技术演讲或幻灯片
- 带动画效果的语法高亮代码片段
- 交互式演示（Monaco 编辑器、可运行代码）
- 数学公式（LaTeX）或图表（Mermaid、PlantUML）
- 配合演讲者备注进行录制
- 导出为 PDF、PPTX，或作为 SPA 托管
- 面向开发者演讲或工作坊的代码讲解

## 快速开始

```bash
pnpm create slidev    # 创建项目
pnpm run dev          # 启动开发服务器（打开 http://localhost:3030）
pnpm run build        # 构建静态 SPA
pnpm run export       # 导出为 PDF（需要 playwright-chromium）
```

**验证**：执行 `pnpm run dev` 后，确认幻灯片能在 `http://localhost:3030` 正常打开。执行 `pnpm run export` 后，检查项目根目录下是否生成了输出 PDF。

## 基础语法

```md
---
theme: default
title: 我的演示文稿
---

# 第一页

这里是内容

---

# 第二页

更多内容

<!--
这里填写演讲者备注
-->
```

- `---` 用于分隔幻灯片
- 第一段 frontmatter = headmatter（整套幻灯片配置）
- HTML 注释 = 演讲者备注

## 核心参考

| 主题 | 说明 | 引用 |
|------|------|------|
| Markdown 语法 | 幻灯片分隔、frontmatter、备注、代码块 | [core-syntax](references/core-syntax.md) |
| 动画 | v-click、v-clicks、motion、过渡 | [core-animations](references/core-animations.md) |
| Headmatter | 整套幻灯片级别的配置项 | [core-headmatter](references/core-headmatter.md) |
| Frontmatter | 单页幻灯片的配置项 | [core-frontmatter](references/core-frontmatter.md) |
| CLI 命令 | 开发、构建、导出、主题命令 | [core-cli](references/core-cli.md) |
| 组件 | 内置 Vue 组件 | [core-components](references/core-components.md) |
| 布局 | 内置幻灯片布局 | [core-layouts](references/core-layouts.md) |
| 导出 | PDF、PPTX、PNG 导出选项 | [core-exporting](references/core-exporting.md) |
| 托管 | 构建并部署到不同平台 | [core-hosting](references/core-hosting.md) |
| 全局上下文 | `$nav`、`$slidev`、composables API | [core-global-context](references/core-global-context.md) |

## 功能速查

### 代码与编辑器

| 功能 | 用法 | 引用 |
|------|------|------|
| 行高亮 | `` ```ts {2,3} `` | [code-line-highlighting](references/code-line-highlighting.md) |
| 基于点击的高亮 | `` ```ts {1\|2-3\|all} `` | [code-line-highlighting](references/code-line-highlighting.md) |
| 行号 | `lineNumbers: true` 或 `{lines:true}` | [code-line-numbers](references/code-line-numbers.md) |
| 可滚动代码块 | `{maxHeight:'100px'}` | [code-max-height](references/code-max-height.md) |
| 代码标签页 | `::code-group`（需要 `comark: true`） | [code-groups](references/code-groups.md) |
| Monaco 编辑器 | `` ```ts {monaco} `` | [editor-monaco](references/editor-monaco.md) |
| 运行代码 | `` ```ts {monaco-run} `` | [editor-monaco-run](references/editor-monaco-run.md) |
| 编辑文件 | `<<< ./file.ts {monaco-write}` | [editor-monaco-write](references/editor-monaco-write.md) |
| 代码动画 | `` ````md magic-move `` | [code-magic-move](references/code-magic-move.md) |
| TypeScript 类型 | `` ```ts twoslash `` | [code-twoslash](references/code-twoslash.md) |
| 导入代码 | `<<< @/snippets/file.js` | [code-import-snippet](references/code-import-snippet.md) |

### 图表与数学

| 功能 | 用法 | 引用 |
|------|------|------|
| Mermaid 图表 | `` ```mermaid `` | [diagram-mermaid](references/diagram-mermaid.md) |
| PlantUML 图表 | `` ```plantuml `` | [diagram-plantuml](references/diagram-plantuml.md) |
| LaTeX 数学公式 | `$inline$` 或 `$$block$$` | [diagram-latex](references/diagram-latex.md) |

### 布局与样式

| 功能 | 用法 | 引用 |
|------|------|------|
| 画布尺寸 | `canvasWidth`、`aspectRatio` | [layout-canvas-size](references/layout-canvas-size.md) |
| 缩放幻灯片 | `zoom: 0.8` | [layout-zoom](references/layout-zoom.md) |
| 缩放元素 | `<Transform :scale="0.5">` | [layout-transform](references/layout-transform.md) |
| 布局插槽 | `::right::`、`::default::` | [layout-slots](references/layout-slots.md) |
| 作用域 CSS | 在幻灯片中写 `<style>` | [style-scoped](references/style-scoped.md) |
| 全局层 | `global-top.vue`、`global-bottom.vue` | [layout-global-layers](references/layout-global-layers.md) |
| 可拖拽元素 | `v-drag`、`<v-drag>` | [layout-draggable](references/layout-draggable.md) |
| 图标 | `<mdi-icon-name />` | [style-icons](references/style-icons.md) |

### 动画与交互

| 功能 | 用法 | 引用 |
|------|------|------|
| 点击动画 | `v-click`、`<v-clicks>` | [core-animations](references/core-animations.md) |
| 手绘标记 | `v-mark.underline`、`v-mark.circle` | [animation-rough-marker](references/animation-rough-marker.md) |
| 绘图模式 | 按 `C` 或配置 `drawings:` | [animation-drawing](references/animation-drawing.md) |
| 方向样式 | `forward:delay-300` | [style-direction](references/style-direction.md) |
| 备注高亮 | 在备注中使用 `[click]` | [animation-click-marker](references/animation-click-marker.md) |

### 语法扩展

| 功能 | 用法 | 引用 |
|------|------|------|
| Comark 语法 | `comark: true` + `{style="color:red"}` | [syntax-mdc](references/syntax-mdc.md) |
| 块级 frontmatter | 用 `` ```yaml `` 替代 `---` | [syntax-block-frontmatter](references/syntax-block-frontmatter.md) |
| 导入幻灯片 | `src: ./other.md` | [syntax-importing-slides](references/syntax-importing-slides.md) |
| 合并 frontmatter | 主入口优先 | [syntax-frontmatter-merging](references/syntax-frontmatter-merging.md) |

### 演讲者与录制

| 功能 | 用法 | 引用 |
|------|------|------|
| 录制 | 按 `G` 打开摄像头 | [presenter-recording](references/presenter-recording.md) |
| 计时器 | `duration: 30min`、`timer: countdown` | [presenter-timer](references/presenter-timer.md) |
| 远程控制 | `slidev --remote` | [presenter-remote](references/presenter-remote.md) |
| Ruby 注音 | `notesAutoRuby:` | [presenter-notes-ruby](references/presenter-notes-ruby.md) |

### 导出与构建

| 功能 | 用法 | 引用 |
|------|------|------|
| 导出选项 | `slidev export` | [core-exporting](references/core-exporting.md) |
| 构建与部署 | `slidev build` | [core-hosting](references/core-hosting.md) |
| 构建时附带 PDF | `download: true` | [build-pdf](references/build-pdf.md) |
| 缓存图片 | 自动处理远程 URL | [build-remote-assets](references/build-remote-assets.md) |
| OG 图片 | `seoMeta.ogImage` 或 `og-image.png` | [build-og-image](references/build-og-image.md) |
| SEO 标签 | `seoMeta:` | [build-seo-meta](references/build-seo-meta.md) |

**导出前置条件**：导出 PDF/PPTX/PNG 需要先执行 `pnpm add -D playwright-chromium`。如果导出时出现浏览器相关错误，先安装这个依赖。

### 编辑器与工具

| 功能 | 用法 | 引用 |
|------|------|------|
| 侧边编辑器 | 点击编辑图标 | [editor-side](references/editor-side.md) |
| VS Code 扩展 | 安装 `antfu.slidev` | [editor-vscode](references/editor-vscode.md) |
| Prettier | `prettier-plugin-slidev` | [editor-prettier](references/editor-prettier.md) |
| 弹出主题 | `slidev theme eject` | [tool-eject-theme](references/tool-eject-theme.md) |

### 生命周期与 API

| 功能 | 用法 | 引用 |
|------|------|------|
| 幻灯片钩子 | `onSlideEnter()`、`onSlideLeave()` | [api-slide-hooks](references/api-slide-hooks.md) |
| 导航 API | `$nav`、`useNav()` | [core-global-context](references/core-global-context.md) |

## 常见布局

| 布局 | 用途 |
|------|------|
| `cover` | 标题页 / 封面页 |
| `center` | 内容居中 |
| `default` | 标准幻灯片 |
| `two-cols` | 双栏布局（使用 `::right::`） |
| `two-cols-header` | 标题 + 双栏 |
| `image` / `image-left` / `image-right` | 图片布局 |
| `iframe` / `iframe-left` / `iframe-right` | 嵌入 URL |
| `quote` | 引用页 |
| `section` | 章节分隔页 |
| `fact` / `statement` | 数据 / 结论展示 |
| `intro` / `end` | 开场 / 结束页 |

## 资源

- 文档：https://sli.dev
- 主题画廊：https://sli.dev/resources/theme-gallery
- 案例展示：https://sli.dev/resources/showcases
