---
theme: default
layout: cover
background: https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1920
---

# Hello, World!

<div class="flex items-center justify-between">
  <div class="text-white bg-blue-500 bg-opacity-50 p-4">Welcome to Tailwind</div>
</div>

---
layout: default
---

<div class="flex items-center justify-between">
  <div class="bg-blue-500 text-white p-4 rounded-lg">Item 1</div>
  <div class="bg-blue-500 text-white p-4 rounded-lg">Item 2</div>
</div>

<br>

<div class="border-2 rounded-lg p-4 shadow-lg">
  <p>This box has a border and rounded corners.</p>
</div>

<br>

<button class="hover:bg-blue-500 rounded-md">
  Hover or Focus Me!
</button>

<br>

<!-- 创建 3 列的布局 -->
<div class="columns-3 flex space-x-5">
  <p>Column 1</p>
  <p>Column 2</p>
  <p>Column 3</p>
</div>

<div class="flex">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

---
layout: default
---

<h1 class="text-shadow-lg">带阴影的标题</h1>

<div class="grid grid-cols-3 gap-4">
  <div class="...">01</div>
  <div class="...">02</div>
  <div class="...">03</div>
  <div class="col-span-2 ...">04</div>
  <div class="...">05</div>
  <div class="...">06</div>
  <div class="col-span-2 ...">07</div>
</div>
