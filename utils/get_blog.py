# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:43
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_blog.py
import json

# 博客
def getblog():
    with open('data/blog.json','r',encoding='utf-8')as f:
        data = json.load(f)
        return data