---
name: frontmatter
description: 单页幻灯片的配置项
---

# 单页 Frontmatter

单页幻灯片的配置项。

## 布局

```yaml
---
layout: center
---
```

可用布局：`default`、`cover`、`center`、`two-cols`、`two-cols-header`、`image`、`image-left`、`image-right`、`iframe`、`iframe-left`、`iframe-right`、`quote`、`section`、`statement`、`fact`、`full`、`intro`、`end`、`none`

## 背景

```yaml
---
background: /image.jpg
backgroundSize: cover
class: text-white
---
```

## 点击次数

```yaml
---
clicks: 5                   # 本页总点击数
clicksStart: 0              # 起始点击编号
---
```

## 过渡

```yaml
---
transition: fade            # 幻灯片过渡
---
```

或分别设置前进 / 后退过渡：

```yaml
---
transition: slide-left | slide-right
---
```

## 缩放

```yaml
---
zoom: 0.8                   # 缩放内容（0.8 = 80%）
---
```

## 隐藏幻灯片

```yaml
---
disabled: true              # 隐藏这一页
# 或
hide: true
---
```

## 目录

```yaml
---
hideInToc: true             # 不在 Toc 组件中显示
level: 2                    # 覆盖标题层级
title: 自定义标题           # 覆盖幻灯片标题
---
```

## 导入外部文件

```yaml
---
src: ./slides/intro.md      # 导入 markdown 文件
---
```

指定导入某几页：

```yaml
---
src: ./other.md#2,5-7       # 导入第 2、5、6、7 页
---
```

## 路由别名

```yaml
---
routeAlias: intro           # URL: /intro 而不是 /1
---
```

## 预加载

```yaml
---
preload: false              # 进入前不挂载
---
```

## 可拖拽位置

```yaml
---
dragPos:
  logo: 100,50,200,100,0    # 左,上,宽,高,旋转
  arrow: 300,200,50,50,45
---
```

## 图片布局

```yaml
---
layout: image-left
image: /photo.jpg
backgroundSize: contain
class: my-custom-class
---
```

## Iframe 布局

```yaml
---
layout: iframe
url: https://example.com
---
```

## 双栏

```yaml
---
layout: two-cols
---

# 左侧

内容

::right::

# 右侧

内容
```

## 带标题的双栏

```yaml
---
layout: two-cols-header
---

# 标题

::left::

左侧内容

::right::

右侧内容
```

## 完整示例

```yaml
---
layout: center
background: /bg.jpg
class: text-white text-center
transition: fade
clicks: 3
zoom: 0.9
hideInToc: false
---

# 幻灯片内容
```
