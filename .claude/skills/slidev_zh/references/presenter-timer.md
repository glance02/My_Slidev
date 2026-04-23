---
name: presenter-timer
description: 演讲者模式中的计时器和进度条
---

# 演讲者计时器

演讲者模式中的计时器和进度条。

## 配置

```yaml
---
duration: 30min
timer: stopwatch
---
```

## 选项

- `duration`：演讲时长（默认：`30min`）
- `timer`：模式，可选 `stopwatch` 或 `countdown`（默认：`stopwatch`）

## 功能

- 开始、暂停、重置控制
- 通过进度条显示已用 / 剩余时间
- 仅在演讲者模式可见

## 时长格式

- `30min` - 30 分钟
- `1h` - 1 小时
- `45min` - 45 分钟
