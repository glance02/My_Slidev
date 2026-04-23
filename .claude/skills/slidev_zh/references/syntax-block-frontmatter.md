---
name: block-frontmatter
description: 使用 YAML 代码块作为幻灯片 frontmatter，以获得语法高亮
---

# 块级 Frontmatter

当你希望获得语法高亮和格式化支持时，可以使用 YAML 代码块作为幻灯片的 frontmatter。

## 用法

不使用传统的 frontmatter `---`，而是在幻灯片开头写一个 yaml 代码块：

````md
---
theme: default
---

# 幻灯片 1

---

```yaml
layout: quote
```

# 幻灯片 2

---

# 幻灯片 3
````

## 关键点

- 仅适用于单页 frontmatter
- 不能用于整套幻灯片的 headmatter（第一段 frontmatter）
- 能在编辑器中获得语法高亮
- 与 `prettier-plugin-slidev` 兼容
