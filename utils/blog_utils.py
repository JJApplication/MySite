# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:44
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_utils.py

from functools import reduce
import re,math
from running_data import bloglist


# 博客的md文件处理函数
def read_md(file):
    with open(file,encoding='utf-8')as md_file:
        content = reduce(lambda x,y: x+y,md_file.readlines())

    return content

def blog_title(content):

    title = re.search(r'title: (.*)',content,re.M|re.I)
    return title.group(1)

def blog_content(content):

    post = re.sub(r'^---\n.*^---$',"",content,0,re.M|re.S)
    return post

def blog_date(content):

    date = re.search(r'date: (.*) ',content,re.M|re.I)
    return date.group(1)

def abstract(content):
        # 摘要文字
        txt = blog_content(content)
        abstract = re.search(r'(.*)<!--more-->',txt,re.M|re.S|re.I).group(1)

        return abstract
def tag(content):
    #标签
    try:
        tags = re.search(r'^tags:\n(.*)\ncategories',content,re.M|re.I|re.S).group(1)
        tags = tags.replace('\n','').replace(' ','').split('-')[1:]
    except:
        tags = ['暂时没有标签']
    return tags

# 计算文章总数和页面分页
def calcblog(n,length):
    length = length + 1

    page = math.ceil(length/7) #总页数
    pagelist = []
    if n < 3:
        pagelist = [1,2,3,page-1,page]

    elif 3 <= n < page-2:
        pagelist = [1,n,n+1,page-1,page]
    elif page-2 <= n <page-1:
        pagelist = [1,2,n,page-1,page]
    elif n >= page-1:
        pagelist = [1,2,3,page-1,page]


    return pagelist