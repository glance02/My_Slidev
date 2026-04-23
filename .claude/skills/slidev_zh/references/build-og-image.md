---
name: og-image
description: 配置社交分享时的 Open Graph 预览图
---

# Open Graph 图片

设置社交媒体分享时使用的预览图。

## 自定义 URL

```md
---
seoMeta:
  ogImage: https://url.to.your.image.png
---
```

## 本地图片

将 `./og-image.png` 放在项目根目录，Slidev 会自动使用它。

## 自动生成

从第一页幻灯片生成：

```md
---
seoMeta:
  ogImage: auto
---
```

它会使用 Playwright 截取第一页，因此需要先安装 playwright。

生成后的图片会保存为 `./og-image.png`，可以直接提交到仓库。
