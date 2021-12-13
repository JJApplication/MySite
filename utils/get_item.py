# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:41
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_item.py

def getitem(theme,data):
    list = []
    for d in data:
        if d["theme"] == theme:
            list.append(d)

    return list