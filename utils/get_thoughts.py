# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:40
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_thoughts.py

# 想法
import json

def getthoughts():
    with open('data/thoughts.json','r',encoding='utf-8')as f:
        data = json.load(f)
        f.flush()
        f.close()
    return data