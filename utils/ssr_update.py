# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:39
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: ssr_update.py
import json

# ssr抓取
def update():
    with open('data/data.json','r')as f:
        data = json.load(f)
        f.flush()
        f.close()
    return data