---
name: importing-slides
description: 将演示拆分为多个文件以提高复用性
---

# 导入幻灯片

将演示拆分为多个文件，以提高复用性。

## 基础导入

```md
# 标题

这是普通页面

---
src: ./pages/toc.md
---

<!-- 这里的内容会被忽略 -->

---

# 第 4 页

另一个普通页面
```

## 导入指定页

使用 hash 选择幻灯片：

```md
---
src: ./another-presentation.md#2,5-7
---
```

会导入第 2、5、6、7 页。

## 复用幻灯片

同一个文件可以导入多次：

```md
---
src: ./pages/toc.md
---

<!-- 后面还可以继续... -->

---
src: ./pages/toc.md
---
```

## Frontmatter 优先级

如果有重复键，主入口文件中的 frontmatter 会覆盖被导入文件中的 frontmatter。
