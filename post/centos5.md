---
title: Centos查看端口占用
date: 2019-03-26 23:09:52
tags:
  - linux
categories:
  - linux
abstract: linux下如何查看端口被哪些程序占用
---

```bash
lsof -i:8888
#查看端口的占用程序
```

```bash
netstat -tunlp |grep 8888
#查看端口的进程情况
```

<!--more-->