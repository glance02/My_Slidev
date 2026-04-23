---
name: pdf
description: 在 SPA 构建产物中附带可下载的 PDF
---

# 构建时生成 PDF

在构建后的幻灯片旁边生成一个可下载的 PDF。

## 在 Headmatter 中启用

```md
---
download: true
---
```

这会生成 PDF，并在构建后的幻灯片中加入下载按钮。

## 自定义 PDF URL

跳过生成流程，直接使用现成的 PDF：

```md
---
download: 'https://example.com/my-talk.pdf'
---
```

## CLI 选项

```bash
slidev build --download
```

## 导出选项

可通过以下方式配置 PDF 导出设置：
- CLI：`slidev build --download --with-clicks --timeout 60000`
- Headmatter：设置 `exportFilename`、`withClicks` 等字段
