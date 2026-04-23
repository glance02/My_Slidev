---
name: components
description: Slidev 中开箱即用的组件
---

# 内置组件

Slidev 中开箱即用的组件。

## 导航

### Link

跳转到指定幻灯片：
```md
<Link to="5">跳到第 5 页</Link>
<Link to="intro">跳到 intro</Link>  <!-- 配合 routeAlias -->
```

### SlideCurrentNo / SlidesTotal

```md
第 <SlideCurrentNo /> 页，共 <SlidesTotal /> 页
```

### Toc（目录）

```md
<Toc />
<Toc maxDepth="2" />
<Toc columns="2" />
```

Props：
- `columns` - 列数
- `maxDepth` / `minDepth` - 标题层级过滤
- `mode` - `'all'` | `'onlyCurrentTree'` | `'onlySiblings'`

### TitleRenderer

渲染指定幻灯片标题：
```md
<TitleRenderer no="3" />
```

## 动画

### VClick / VClicks

```md
<VClick>点击后显示</VClick>

<VClicks>

- 项目 1
- 项目 2

</VClicks>
```

### VAfter

```md
<VClick>第一项</VClick>
<VAfter>与第一项同时显示</VAfter>
```

### VSwitch

```md
<VSwitch>
  <template #1>状态 1</template>
  <template #2>状态 2</template>
</VSwitch>
```

## 绘图

### Arrow

```md
<Arrow x1="10" y1="10" x2="100" y2="100" />
<Arrow x1="10" y1="10" x2="100" y2="100" two-way />
```

Props：`x1`、`y1`、`x2`、`y2`、`width`、`color`、`two-way`

### VDragArrow

可拖拽箭头：
```md
<VDragArrow />
```

## 布局

### Transform

缩放元素：
```md
<Transform :scale="0.5">
  <LargeContent />
</Transform>
```

Props：`scale`、`origin`

### AutoFitText

自动适应尺寸的文本：
```md
<AutoFitText :max="200" :min="50" modelValue="Hello" />
```

## 媒体

### SlidevVideo

```md
<SlidevVideo v-click autoplay controls>
  <source src="/video.mp4" type="video/mp4" />
</SlidevVideo>
```

Props：`controls`、`autoplay`、`autoreset`、`poster`、`timestamp`

### Youtube

```md
<Youtube id="dQw4w9WgXcQ" />
<Youtube id="dQw4w9WgXcQ" width="600" height="400" />
```

### Tweet

```md
<Tweet id="1423789844234231808" />
<Tweet id="1423789844234231808" :scale="0.8" />
```

## 条件渲染

### LightOrDark

```md
<LightOrDark>
  <template #dark>深色模式内容</template>
  <template #light>浅色模式内容</template>
</LightOrDark>
```

### RenderWhen

```md
<RenderWhen context="presenter">
  仅在演讲者模式显示
</RenderWhen>
```

可用 context 值：
- `main` - 主演示视图
- `visible` - 可见幻灯片
- `print` - 打印 / 导出模式
- `slide` - 普通幻灯片视图
- `overview` - 总览模式
- `presenter` - 演讲者模式
- `previewNext` - 下一页预览

## 品牌

### PoweredBySlidev

```md
<PoweredBySlidev />
```

## 拖拽

### VDrag

```md
<VDrag pos="myElement">
  可拖拽内容
</VDrag>
```

详细说明见 [draggable](layout-draggable.md)。

## 组件自动导入

以下来源的组件会自动导入：
1. 内置组件
2. 主题组件
3. 插件组件
4. `./components/` 目录

无需手写 import 语句。
