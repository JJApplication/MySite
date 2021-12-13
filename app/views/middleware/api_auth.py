# -*- coding: utf-8 -*-
# Time: 2020-08-18 0:07
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: api_auth.py

from . import mypage
from flask import request,abort

@mypage.before_request
def api_auth():
    uri = request.path
    refer = request.referrer if request.referrer else "127.0.0.1"
    host = request.host if request.host else "127.0.0.1"
    if uri == '/api/unsub':
        pass
    elif '/api/' in uri:
        if not refer or "127.0.0.1" in refer or "127.0.0.1" in host:
            abort(403)
        elif "mgek.cc" in refer or "renj.io" in refer:
            pass
        else:
            abort(403)
    else:
        pass