---
title: simulink对QPSK信号进行OFDM仿真
date: 2019-06-13 23:29:53
tags:
  - matlab
categories:
  - matlab
abstract:
---

**matlab实验**

使用simulink对信号进行OFDM仿真，考虑信号在经过高斯噪声信道和瑞利多径衰落后误码率比较

![VhHOHK.png](http://file.mgek.cc/images/blog/matlab9-1.webp)


<!--more-->

结果

使用随机数发生器，产生需要的信号。信号码率为1000b/s，噪声信道添加75db的噪声

![VhLcjA.png](http://file.mgek.cc/images/blog/matlab9-2.webp)

![VhL6cd.png](http://file.mgek.cc/images/blog/matlab9-3.webp)

