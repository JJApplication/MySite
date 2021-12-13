---
title: 前端入门-html基础
date: 2020-12-04 22:44:35
tags:
  - html
categories:
  - html
abstract:
---

前端学习-html基础知识

<!--more-->

什么是前端？曾经我一直以为会写html页面，会整几个css样式，会用几个web前端框架就算是前端了

逐渐深入才发现，远远不止这些，html块级元素之间的关系，层级结构。css的渲染方式以及css复用规则，类名的复用设计等等这些都是平时开发时没有注意的

# html

完整参考**MDN**官方的html元素定义

HTML 不是一门编程语言，而是一种用于定义内容结构的*标记语言*。HTML 由一系列的**元素（[elements](https://developer.mozilla.org/zh-CN/docs/Glossary/元素)）**组成，这些元素可以用来包围不同部分的内容，使其以某种方式呈现或者工作。

## 类和id的定义标准

在标签内是可以为元素添加类名和标签的，根据`html`的规范，类名统一为`小写字母-小写字母`方式，id为小驼峰形式

**注意一般使用双引号包裹属性**

例如：

```html
<p class="top-text" id="topBanner">
    hello
</p>
```



### 常见html元素

```html
<p>welcome to jj's blog!</p>
```

渲染结果：

<p>welcome to jj's blog!</p>

段落元素一般包含开始标签，内容，结束标签。他们共同构成了元素

### 嵌套元素

何为嵌套，即在元素内部写另一个元素

```html
<p>welcome <strong>to</strong> jj's blog!</p>
```

渲染结果：

<p>welcome <strong>to</strong> jj's blog!</p>

这里的`strong`标签就是可以嵌套的元素，因为是嵌套关系所以`strong`的闭合在`p`标签的内部

### 空元素

没有任何内容的元素，比如`img`，十分特殊的是`img`没有结束标签

```html
<img src="" alt="">
```

`alt`属性比较特殊是图片的描述内容，当图片不可见时可以看到内部的内容。`alt` 文本应向用户完整地传递图像要表达的意思

## html文档结构

以最新的HTML5标准

首行为文档版本声明，依次为`html`，`head`，`body`。head头中包含`meta`标签，`title`标签，`link`标签，`script`标签等

页面的主要内容放在`body`体内部，该元素包含了期望用户看到的内容

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>测试页面</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="测试图片">
  </body>
</html>
```

### 标记文本

什么是标记文本？类似作文的标题或者word的不同级别的标题

从1-6分为6各层级由`<h1>-<h6>`

```html
<h1>主标题</h1>
<h2>顶层标题</h2>
<h3>子标题</h3>
<h4>次子标题</h4>
```

渲染结果：

<h1>主标题</h1>
<h2>顶层标题</h2>
<h3>子标题</h3>
<h4>次子标题</h4>

> 注意：标题的意义十分重大，不要使用标题的方式来放大加粗字体，而是使用style样式。标题对于搜索引擎的SEO十分重要。
>
> 所以一般标题一都是一片文章内容的第一行。保持标题的整洁不要出现标题越级的情况
>
> 比如: `<h1></h1> <h3></h3>`

### 段落

一般段落是网页的常规文本内容

```html
<p>这是一个段落</p>
```

### 列表

网页可以展示形如word表格的列表元素。一般至少包含两个元素，分为**无序列表**，**有序列表**

每一个列表项目都用`<li>`标签包裹

```html
<!--无序列表-->
<ul> 
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ul>

<!--有序列表-->
<ol> 
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ol>
```

渲染结果：

<!--无序列表-->

<ul> 
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ul>


<!--有序列表-->

<ol> 
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ol>

### 链接

网页上可以点击跳转的链接元素，`<a>`成为锚

```html
<a href="">Mozilla 宣言</a>
<a href="https://www.google.com" target="_blank">打开Google</a>
```

当`href`属性为空时或者不存在此属性时，它并不会有任何操作

如果网址开始部分省略了 `https://` 或者 `http://`，可能会得到错误的结果。在完成一个链接后，可以试着点击它来确保指向正确。

渲染结果：

<a href="https://www.google.com" target="_blank">打开Google</a>

## 其他标签

### 块元素div

定义文档区域，文档布局

```html
<div id="id名" class="class名"></div>
```

### 按钮input

input根据属性分为多种功能

```html
<input  name=""  type="button" value=“按钮内容” />
```

### 多行文本textarea

```html
<textarea name="textareal" cols="字符宽度" rows="行数"></textarea>
```

### 下拉菜单select

```html
<select  name="">
  <option>菜单内容</option>
</select>
```

### 复选框checkbox

一般为input的属性

```html
<input type="checkbox" name="like" />
<input type="checkbox" name="like" disabled="disabled" />
(disabled="disabled" :禁用)
(checked="checked" :默认选中)
```

### 单选按钮

单选按钮里的name属性必须写，同一组单选按钮的name属性值必须一样。

```html
<input type="radio" name="ral"/>
<input type="radio" name="ral"/>

checked="checked"(默认选中；)
disabled="disabled"禁用
```

### 文本框

```html
<input type="text" value="默认值"/>
```

### 密码框

```html
<input type="password" />
```

### 提交按钮

```html
<input type="submit" value="按钮内容" />
```

### 重置按钮

```html
<input type="reset" value="按钮内容" />
```

### 表单form

常搭配input一起使用

```html
<form name="表单名称" method="post/get"  action=""></form>
```

### 数据表格table

一个`tr`表示一行;一个`td`表示一列(一个单元格)

```html
<table >
<tr>
  <td></td>
  <td></td>
</tr>
</table>
```

## 不常见标签

### 加粗b

```html
1).<b>加粗内容</b>
2).<strong>加粗内容</strong>
```

### 斜体元素

```html
1.<em></em>(emphasized )
2,<i></i>( italic )
```

### 换行br

```html
<br />
```

### 水平线hr

```html
<hr />空标记(horizontal   rule)
```

### 上标文本

```html
<sup></sup>
```

### 删除线

```html
<del></del>
```

