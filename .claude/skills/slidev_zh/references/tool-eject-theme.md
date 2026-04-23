---
name: eject-theme
description: 将主题提取到本地文件系统中以便自定义
---

# 弹出主题

将已安装的主题提取到本地文件系统中，以便自定义。

## 命令

```bash
slidev theme eject
```

## 结果

- 主题文件会被复制到 `./theme/`
- frontmatter 会更新为 `theme: ./theme`

## 使用场景

- 完全掌控主题
- 基于已有主题创建新主题
- 在不修改 `node_modules` 的前提下进行定制

如果你要创建衍生主题，请注明原主题及作者。
