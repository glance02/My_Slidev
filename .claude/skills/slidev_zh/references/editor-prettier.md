---
name: prettier-plugin
description: 正确格式化 Slidev Markdown 文件
---

# Prettier 插件

正确格式化 Slidev Markdown 文件。

## 安装

```bash
pnpm i -D prettier prettier-plugin-slidev
```

## 配置

创建或修改 `.prettierrc`：

```json
{
  "overrides": [
    {
      "files": ["slides.md", "pages/*.md"],
      "options": {
        "parser": "slidev",
        "plugins": ["prettier-plugin-slidev"]
      }
    }
  ]
}
```

## 为什么需要它

Slidev 的语法（frontmatter、代码块等）可能会和默认 Markdown 格式化规则冲突。这个插件能理解 Slidev 专属语法。

## 注意

由于 Slidev 和普通 Markdown 都使用 `.md` 扩展名，所以必须通过 `overrides` 显式指定文件。
