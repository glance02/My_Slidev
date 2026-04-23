---
name: slot-sugar
description: 多列布局中为具名插槽提供简写语法
---

# 布局插槽简写

用于具名布局插槽的简写语法。

## 标准 Vue 插槽语法

```md
---
layout: two-cols
---

<template v-slot:default>

# 左侧

这里显示在左边

</template>
<template v-slot:right>

# 右侧

这里显示在右边

</template>
```

## 简写语法

```md
---
layout: two-cols
---

# 左侧

这里显示在左边

::right::

# 右侧

这里显示在右边
```

## 显式 default 插槽

```md
---
layout: two-cols
---

::right::

# 右侧

这里显示在右边

::default::

# 左侧

这里显示在左边
```

## 常见带插槽的布局

- `two-cols`：`default`（左侧）和 `right`
- `two-cols-header`：`default`、`left`、`right`
- `image-left/right`：`default` 用于内容区
