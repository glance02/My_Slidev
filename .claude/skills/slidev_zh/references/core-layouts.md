---
name: layouts
description: 幻灯片可用的布局
---

# 内置布局

幻灯片可用的布局。

## 基础布局

### default

标准幻灯片布局。
```yaml
---
layout: default
---
```

### center

内容水平和垂直居中。
```yaml
---
layout: center
---
```

### cover

标题 / 封面页布局，内容居中。
```yaml
---
layout: cover
---
```

### end

结束页。
```yaml
---
layout: end
---
```

### full

全屏内容，无内边距。
```yaml
---
layout: full
---
```

### none

不应用任何布局样式。
```yaml
---
layout: none
---
```

## 文本布局

### intro

介绍页。
```yaml
---
layout: intro
---
```

### quote

大号引用展示。
```yaml
---
layout: quote
---
```

### section

章节分隔页。
```yaml
---
layout: section
---
```

### statement

结论 / 陈述展示。
```yaml
---
layout: statement
---
```

### fact

事实 / 数据展示。
```yaml
---
layout: fact
---
```

## 多列布局

### two-cols

左右双栏：
```md
---
layout: two-cols
---

# 左栏

左侧内容

::right::

# 右栏

右侧内容
```

### two-cols-header

上方标题，下方双栏：
```md
---
layout: two-cols-header
---

# 标题

::left::

左侧内容

::right::

右侧内容
```

## 图片布局

### image

全屏图片：
```yaml
---
layout: image
image: /photo.jpg
backgroundSize: cover
---
```

### image-left

左图右文：
```yaml
---
layout: image-left
image: /photo.jpg
class: my-class
---

# 右侧内容
```

### image-right

右图左文：
```yaml
---
layout: image-right
image: /photo.jpg
---

# 左侧内容
```

Props：`image`、`class`、`backgroundSize`

## Iframe 布局

### iframe

全屏 iframe：
```yaml
---
layout: iframe
url: https://example.com
---
```

### iframe-left

左侧 iframe，右侧内容：
```yaml
---
layout: iframe-left
url: https://example.com
---

# 内容
```

### iframe-right

右侧 iframe，左侧内容：
```yaml
---
layout: iframe-right
url: https://example.com
---

# 内容
```

## 布局加载顺序

1. Slidev 默认布局
2. 主题布局
3. 插件布局
4. 自定义布局（`./layouts/`）

越靠后的来源优先级越高，会覆盖前面的布局。

## 自定义布局

创建 `layouts/my-layout.vue`：

```vue
<template>
  <div class="slidev-layout my-layout">
    <slot />
  </div>
</template>

<style scoped>
.my-layout {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
```

使用具名插槽：

```vue
<template>
  <div class="slidev-layout two-areas">
    <div class="top">
      <slot name="top" />
    </div>
    <div class="bottom">
      <slot />
    </div>
  </div>
</template>
```

用法：
```md
---
layout: two-areas
---

::top::

顶部内容

::default::

底部内容
```
