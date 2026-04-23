---
name: direction
description: 基于导航方向应用不同样式
---

# 导航方向变体

根据导航方向（前进 / 后退）应用不同样式。

## CSS 类

```css
/* 仅在向前导航时延迟 */
.slidev-nav-go-forward .slidev-vclick-target {
  transition-delay: 500ms;
}
.slidev-nav-go-backward .slidev-vclick-target {
  transition-delay: 0;
}
```

## UnoCSS 变体

使用 `forward:` 或 `backward:` 前缀：

```html
<div v-click class="transition forward:delay-300">元素</div>
```

这样只有前进时会延迟动画，返回时不会延迟。

## 使用场景

适合制作非对称动画，让进入幻灯片和离开幻灯片有不同的观感。
