---
name: remote-assets
description: 打包远程图片和资源，便于离线使用
---

# 打包远程资源

远程图片会在首次运行时自动缓存，以加快后续加载速度。

## 远程图片

```md
![远程图片](https://sli.dev/favicon.png)
```

这些资源会由 `vite-plugin-remote-assets` 自动缓存。

## 本地图片

把图片放到 `public/` 目录，并使用以斜杠开头的路径引用：

```md
![本地图片](/pic.png)
```

不要使用 `./pic.png` 这样的相对路径。

## 自定义样式

如果要自定义尺寸或样式，可以改用 `img` 标签：

```html
<img src="/pic.png" class="m-40 h-40 rounded shadow" />
```
