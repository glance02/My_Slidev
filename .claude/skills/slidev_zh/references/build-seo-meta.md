---
name: seo-meta
description: 配置 SEO 与社交媒体 meta 标签
---

# SEO Meta 标签

配置社交媒体与搜索引擎使用的 meta 标签。

## 配置

```yaml
---
seoMeta:
  ogTitle: Slidev Starter Template
  ogDescription: Presentation slides for developers
  ogImage: https://cover.sli.dev
  ogUrl: https://example.com
  twitterCard: summary_large_image
  twitterTitle: Slidev Starter Template
  twitterDescription: Presentation slides for developers
  twitterImage: https://cover.sli.dev
  twitterSite: username
  twitterUrl: https://example.com
---
```

## 可用选项

**Open Graph（Facebook、LinkedIn）：**
- `ogTitle` - 标题
- `ogDescription` - 描述
- `ogImage` - 预览图 URL
- `ogUrl` - 规范链接 URL

**Twitter Card：**
- `twitterCard` - 卡片类型（`summary`、`summary_large_image`）
- `twitterTitle` - 标题
- `twitterDescription` - 描述
- `twitterImage` - 预览图 URL
- `twitterSite` - Twitter 用户名

底层由 unhead 提供支持。
