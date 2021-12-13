# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:16
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: docs.py

from . import mypage
from . import api_docs
from flask import render_template,send_from_directory

@mypage.route(api_docs)
def docs():

    return render_template('docs.html')

@mypage.route(api_docs + '/<string:name>')
def docsdetail(name):

    return send_from_directory('./static/res/mgek/',name+'.html')