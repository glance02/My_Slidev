---
name: exporting
description: 将演示导出为 PDF、PPTX、PNG 或 Markdown
---

# 导出演示文稿

将演示导出为 PDF、PPTX、PNG 或 Markdown。

## 浏览器导出器

可在 `http://localhost:3030/export` 访问：
- 选择格式和选项
- 预览并下载

## CLI 导出

需要 playwright：
```bash
pnpm add -D playwright-chromium
```

### 导出 PDF

```bash
slidev export
slidev export --output my-slides.pdf
```

### 导出 PowerPoint

```bash
slidev export --format pptx
```

### 导出 PNG

```bash
slidev export --format png
slidev export --format png --range 1-5
```

### 导出 Markdown

```bash
slidev export --format md
```

## 导出选项

### 包含点击步骤

把每次点击都导出成独立页面：
```bash
slidev export --with-clicks
```

### 深色模式

```bash
slidev export --dark
```

### 幻灯片范围

```bash
slidev export --range 1,4-7,10
```

### 目录

导出带可点击大纲的 PDF：
```bash
slidev export --with-toc
```

### 超时时间

适用于渲染较慢的幻灯片：
```bash
slidev export --timeout 60000
```

### 等待

截图前额外等待：
```bash
slidev export --wait 2000
```

### Wait Until

等待条件：
```bash
slidev export --wait-until networkidle   # 默认
slidev export --wait-until domcontentloaded
slidev export --wait-until load
slidev export --wait-until none
```

### 透明背景

```bash
slidev export --omit-background
```

### 自定义浏览器

```bash
slidev export --executable-path /path/to/chrome
```

## Headmatter 选项

```yaml
---
exportFilename: my-presentation
download: true              # 在 build 产物中添加下载按钮
export:
  format: pdf
  timeout: 30000
  withClicks: false
---
```

## 故障排查

### 内容缺失

增加等待时间：
```bash
slidev export --wait 3000 --timeout 60000
```

### 全局层状态不正确

使用 `--per-slide`，或者改用 `slide-top.vue` 而不是 `global-top.vue`。

### Emoji 显示异常

改用系统字体，或在服务器上安装 emoji 字体。

### 在 CI/CD 中导出

安装 playwright 浏览器：
```bash
npx playwright install chromium
```
