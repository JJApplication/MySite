# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:41
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_problems.py

import json

# 学术问题
def getproblems():
    with open('data/problems.json','r',encoding='utf-8')as f:
        data = json.load(f)
        f.flush()
        f.close()
    return data