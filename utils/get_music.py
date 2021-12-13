# -*- coding: utf-8 -*-
# Time: 2020-08-02 20:42
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_music.py
import json

# 音乐
def getmusic():
    with open('data/music.json','r',encoding='utf-8')as f:
        data = json.load(f)
        f.close()
        return data