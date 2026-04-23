---
name: slide-hooks
description: 幻灯片组件的生命周期钩子
---

# 幻灯片钩子

幻灯片组件的生命周期钩子。

## 可用钩子

```ts
import { onSlideEnter, onSlideLeave, useIsSlideActive } from '@slidev/client'

const isActive = useIsSlideActive()

onSlideEnter(() => {
  // 当幻灯片变为激活状态时调用
})

onSlideLeave(() => {
  // 当幻灯片变为非激活状态时调用
})
```

## 重要说明

不要在幻灯片中使用 `onMounted` / `onUnmounted`，因为即使幻灯片未激活，组件实例仍会持续存在。

请改用 `onSlideEnter` 和 `onSlideLeave`。

## 使用场景

- 启动 / 停止动画
- 播放 / 暂停媒体
- 初始化 / 清理资源
- 记录分析事件
