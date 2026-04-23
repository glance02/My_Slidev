---
name: hosting
description: 构建并部署 Slidev 演示文稿
---

# 托管与部署

构建并部署 Slidev 演示文稿。

## 生产构建

```bash
slidev build
```

输出：`dist/` 目录（静态 SPA）

### 选项

```bash
slidev build --base /talks/my-talk/    # 自定义基础路径
slidev build --out public              # 自定义输出目录
slidev build --download                # 附带 PDF
slidev build --without-notes           # 不包含备注
```

### 多个演示文件

```bash
slidev build slides1.md slides2.md
```

## GitHub Pages

### GitHub Actions

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 'lts/*'

      - name: Install
        run: npm install

      - name: Build
        run: npm run build -- --base /${{ github.event.repository.name }}/

      - uses: actions/configure-pages@v4

      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

      - uses: actions/deploy-pages@v4
```

## Netlify

创建 `netlify.toml`：

```toml
[build]
  publish = 'dist'
  command = 'npm run build'

[[redirects]]
  from = '/*'
  to = '/index.html'
  status = 200
```

## Vercel

创建 `vercel.json`：

```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

## Docker

### 使用官方镜像

```bash
docker run --name slidev --rm -it \
  -v ${PWD}:/slidev \
  -p 3030:3030 \
  tangramor/slidev:latest
```

### 自定义 Dockerfile

```dockerfile
FROM tangramor/slidev:latest

COPY slides.md .
COPY public ./public

RUN npm run build

EXPOSE 80
CMD ["npx", "serve", "dist"]
```

## 基础路径

适用于部署到子目录：

```bash
# 构建时指定
slidev build --base /my-slides/

# 或在 headmatter 中指定
---
base: /my-slides/
---
```

## 路由模式

如果服务器不支持 rewrite：

```yaml
---
routerMode: hash
---
```

URL 会变成：`/#/1`、`/#/2` 等。
