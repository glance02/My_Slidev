---
name: plantuml
description: 通过文本描述创建 UML 图
---

# PlantUML 图表

通过文本描述创建 UML 图。

## 基础用法

````md
```plantuml
@startuml
Alice -> Bob : Hello!
@enduml
```
````

## 服务器配置

默认使用：https://www.plantuml.com/plantuml

可以在 headmatter 中指定自定义服务器：

```md
---
plantUmlServer: https://your-server.com/plantuml
---
```

## 图表类型

- 时序图
- 类图
- 活动图
- 组件图
- 状态图
- 对象图
- 用例图

## 资源

- PlantUML 文档：https://plantuml.com/
- 在线编辑器：https://plantuml.com/plantuml
