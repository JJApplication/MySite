---
title: Python中的字符串处理
date: 2019-02-28 22:19:34
tags: 
  - python
categories:
  - Python
abstract: python对于字符串的操作实例
---

# 常用的python对于字符串处理<!--more-->

## .format

```python
# 用于格式化字符串
"{0}{1}{0}".format('i','love','u')
>>> ilovei
{0:d} #格式化为整数
{0:s} #格式化为字符串
{0:3f} #保留到小数点后三位浮点数
# 分号： 是用来分隔字符和格式化符的
```

## .join

```python
# 用于拼接符号
','.join('i','love','u')
>>> i,love,u
# 使用，来拼接字符串
```

## .split

```python
# 用于分割字符串
'''ilove'''.split() # 默认使用空格分割
''''''.split(',',2) # 使用逗号分割，分割两次，即拆分为3个字符串
```

## .strip

```python
# 删除不需要的字符
''.strip() # 删除两侧的空格
.rstrip() # 删除右侧的空格
.lstrip()# 删除左侧的空格
.strip('$') # 传入参数，删除$
```

