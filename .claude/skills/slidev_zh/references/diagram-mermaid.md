---
name: mermaid
description: 通过文本描述创建图表
---

# Mermaid 图表

通过文本描述创建图表。

## 基础用法

````md
```mermaid
sequenceDiagram
  Alice->John: Hello John, how are you?
  Note over Alice,John: A typical interaction
```
````

## 搭配选项

````md
```mermaid {theme: 'neutral', scale: 0.8}
graph TD
B[Text] --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```
````

## 图表类型

- `graph` / `flowchart` - 流程图
- `sequenceDiagram` - 时序图
- `classDiagram` - 类图
- `stateDiagram` - 状态图
- `erDiagram` - 实体关系图
- `gantt` - 甘特图
- `pie` - 饼图

## 资源

- Mermaid 文档：https://mermaid.js.org/
- 在线编辑器：https://mermaid.live/
