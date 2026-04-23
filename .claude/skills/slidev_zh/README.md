# Claude Code 的 Slidev 技能

帮助 Claude Code 理解并处理 [Slidev](https://sli.dev) 演示文稿的代理技能集合。

## 安装

```bash
npx skills add slidevjs/slidev
```

这会把 Slidev 技能添加到你的 Claude Code 配置中。

## 包含内容

Slidev 技能会为 Claude Code 提供以下知识：

- **核心语法** - Markdown 语法、幻灯片分隔符、frontmatter
- **动画** - 点击动画、过渡、运动效果
- **代码功能** - 行高亮、Monaco 编辑器、代码分组、magic-move
- **图表** - Mermaid、PlantUML、LaTeX 数学公式
- **布局** - 内置布局、插槽、全局层
- **演讲者模式** - 录制、计时器、远程访问
- **导出** - PDF、PPTX、PNG、SPA 托管

## 用法

安装完成后，Claude Code 会在以下场景中自动使用 Slidev 相关知识：

- 创建新的演示文稿
- 添加带代码示例的幻灯片
- 配置动画和过渡
- 设置主题和布局
- 导出演示文稿

### 示例提示词

```
创建一个关于 TypeScript 泛型的 Slidev 演示文稿，并包含代码示例
```

```
添加一页双栏幻灯片，左边放代码，右边放说明
```

```
设置点击动画，让项目符号逐条显示
```

```
把演示配置成可导出 PDF，并带演讲者备注
```

## 文档

- [Slidev 文档](https://sli.dev)
- [主题画廊](https://sli.dev/resources/theme-gallery)
- [案例展示](https://sli.dev/resources/showcases)

## 许可证

MIT
