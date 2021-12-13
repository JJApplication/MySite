# -*- coding: utf-8 -*-
# Time: 2020-08-04 16:57
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_db.py
from running_data import pin

#博客的输出函数
def generate_list(all):
    blist = []
    try:
        for i in all:
            blist.append(i.pr())
        blist.append(pin)
        return list(reversed(blist))
    except:
        return blist

#输出函数
def get_list(all):
    blist = []
    try:
        for i in all:
            blist.append(i.pr())
        return blist
    except:
        return blist
