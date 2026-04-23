---
name: vscode-extension
description: 在 VS Code 中以可视化方式管理幻灯片
---

# VS Code 扩展

在 VS Code 中以可视化方式管理幻灯片。

## 安装

在 VS Code Marketplace 安装：`antfu.slidev`

## 功能

- 在侧边面板预览幻灯片
- 幻灯片树视图
- 拖拽调整幻灯片顺序
- 按幻灯片块折叠
- 支持多个项目
- 一键启动开发服务器

## 用法

1. 点击活动栏中的 `Slidev` 图标
2. 项目树会显示工作区中的所有 Slidev 项目
3. 幻灯片树会显示当前项目中的所有幻灯片
4. 预览面板会显示实时预览

## 命令

在命令面板中输入 `Slidev` 查看可用命令。

## 配置

把特定文件包含为 Slidev 入口：

```json
{
  "slidev.include": ["**/presentation.md"]
}
```

自定义开发命令：

```json
{
  "slidev.dev-command": "pnpm slidev ${args}"
}
```

## 占位符

- `${args}` - 所有 CLI 参数
- `${port}` - 端口号
