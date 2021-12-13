---
title: hexo向Google提交网站
date: 2019-02-06 18:28:41
tags:
  - hexo
categories:
  - 学习笔记
abstract: 利用Google站长工具提交网站，更快被搜索引擎抓取
---

## 进入Google站长网站，登录自己的谷歌账号

![](http://file.mgek.cc/images/blog/hexo-theme2-1.webp)

选择html文件，在自己的github.io网站下上传html验证文件
<!--more-->

验证通过后进入hexo的目录下，安装sitemap插件

```bash
npm install hexo-generator-sitemap --save
```

修改配置文件_config.yml中的url为自己的网站地址

再次生成静态文件，就会生成站点地图

![](http://file.mgek.cc/images/blog/hexo-theme2-2.webp)

进入谷歌站长的控制台后，选择左侧的站点地图添加地图