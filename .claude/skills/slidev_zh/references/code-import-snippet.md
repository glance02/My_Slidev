---
name: import-snippet
description: 从外部文件导入代码到幻灯片中，并可选指定区域
---

# 导入代码片段

从外部文件把代码导入到幻灯片中。

## 基础语法

```md
<<< @/snippets/snippet.js
```

`@` 表示包根目录。推荐把代码片段放在 `@/snippets/` 下。

## 导入指定区域

使用 VS Code 的 region 语法：

```md
<<< @/snippets/snippet.js#region-name
```

## 指定语言

```md
<<< @/snippets/snippet.js ts
```

## 配合其他功能

可以与行高亮、Monaco 编辑器组合使用：

```md
<<< @/snippets/snippet.js {2,3|5}{lines:true}
<<< @/snippets/snippet.js ts {monaco}{height:200px}
```

## 占位符

行高亮占位时可使用 `{*}`：

```md
<<< @/snippets/snippet.js {*}{lines:true}
```

## Monaco Write

把编辑器和真实文件关联起来，用于实时编辑：

```md
<<< ./some-file.ts {monaco-write}
```
