---
name: zoom-slides
description: 使用 zoom frontmatter 选项缩放单页幻灯片内容
---

# 缩放幻灯片

缩放单页幻灯片内容。

## 用法

```md
---
zoom: 0.8
---

# 一页内容很多的幻灯片

---

# 其他幻灯片不受影响
```

## 取值

- `zoom: 0.8` - 80% 大小（能放下更多内容）
- `zoom: 1.2` - 120% 大小（更大，但能放的内容更少）
- `zoom: 1` - 正常大小（默认）

## 使用场景

- 在一页中容纳较密集的内容
- 提高文字可读性
- 适配不同内容密度

## 相关功能

- 缩放所有幻灯片：在 headmatter 中使用 `canvasWidth` / `aspectRatio`
- 缩放元素：使用 `<Transform>` 组件
