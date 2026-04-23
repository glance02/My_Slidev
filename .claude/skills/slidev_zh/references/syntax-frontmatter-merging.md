---
name: frontmatter-merging
description: 导入幻灯片时，frontmatter 冲突的优先级规则
---

# Frontmatter 合并

导入幻灯片时，主入口文件中的 frontmatter 优先级更高。

## 示例

主文件（`slides.md`）：
```md
---
src: ./cover.md
background: https://sli.dev/bar.png
class: text-center
---
```

被导入文件（`cover.md`）：
```md
---
layout: cover
background: https://sli.dev/foo.png
---

# Cover

Cover Page
```

## 结果

```md
---
layout: cover
background: https://sli.dev/bar.png  # 以主入口为准
class: text-center
---

# Cover

Cover Page
```

## 优先级规则

对于重复键：主入口文件 > 被导入文件。
