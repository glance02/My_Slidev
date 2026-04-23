---
name: monaco-write
description: 编辑代码并把更改直接保存回文件
---

# 可写的 Monaco 编辑器

编辑代码，并把更改直接保存回文件。

## 用法

```md
<<< ./some-file.ts {monaco-write}
```

## 行为

- 将 Monaco 编辑器关联到真实文件
- 修改会直接保存回该文件
- 适合现场编码演示

## 警告

使用前请先备份文件，因为修改会被直接写入。
