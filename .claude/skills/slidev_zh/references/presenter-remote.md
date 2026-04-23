---
name: remote-access
description: 通过局域网或互联网共享演示文稿
---

# 远程访问

通过局域网或互联网共享演示文稿。

## 启用远程访问

```bash
slidev --remote
```

## 密码保护

```bash
slidev --remote=your_password
```

进入演讲者模式时需要输入密码。

## 远程隧道

通过 Cloudflare Quick Tunnels 暴露到公网：

```bash
slidev --remote --tunnel
```

无需额外搭建服务器即可创建公开访问 URL。

## 使用场景

- 用手机 / 平板控制演示
- 多位讲者协作
- 远程演示
- 直播场景
- 让观众在自己的设备上观看
