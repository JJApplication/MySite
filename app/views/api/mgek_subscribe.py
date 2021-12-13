# -*- coding: utf-8 -*-
# Time: 2020-08-18 0:26
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: mgek_subscribe.py

# -*- coding: utf-8 -*-
# Time: 2020-08-17 0:13
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: subscribe.py

from . import mypage
from . import api_ajax_mgek
from flask import jsonify,request
from mail_server.task4 import send_mgek_mail

@mypage.route(api_ajax_mgek,methods=["POST"])
def mgek_subscribe():
    try:
        mail = request.json["mail"]
        opt = send_mgek_mail.apply_async([mail], countdown=30, retry=False)
        if opt:
            return "ok"
        else:
            return "bad"
    except:
        return "bad"
