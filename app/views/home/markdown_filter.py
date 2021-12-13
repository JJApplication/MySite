# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:36
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: markdown_filter.py

from . import mypage
from markdown import markdown


# 博客md文件过滤器
@mypage.app_template_filter('md')
def markdown_to_html(txt):

    return markdown(txt,extensions=['markdown.extensions.fenced_code','markdown.extensions.extra','markdown.extensions.smarty','markdown.extensions.nl2br','markdown.extensions.tables','markdown.extensions.footnotes',
 'markdown.extensions.legacy_attrs','markdown.extensions.admonition'])