---
name: drawing
description: 在演示过程中绘制和标注幻灯片
---

# 绘图与标注

在演示过程中绘制和标注幻灯片。底层由 drauu 驱动。

## 启用绘图

点击导航栏中的画笔图标，或按 `C`。

## 手写笔支持

手写笔设备（iPad + Apple Pencil）会自动工作：用笔绘制，用手指导航。

## 持久化绘图

将绘图保存为 SVG，并包含在导出结果中：

```md
---
drawings:
  persist: true
---
```

绘图会保存到 `.slidev/drawings/`。

## 禁用绘图

完全禁用：
```md
---
drawings:
  enabled: false
---
```

仅在开发环境启用：
```md
---
drawings:
  enabled: dev
---
```

仅在演讲者模式启用：
```md
---
drawings:
  presenterOnly: true
---
```

## 同步设置

禁用多实例之间的同步：

```md
---
drawings:
  syncAll: false
---
```

这样只有演讲者的绘图会同步给其他实例。
