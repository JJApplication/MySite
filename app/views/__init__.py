# -*- coding: utf-8 -*-
# Time: 2020-08-02 19:27
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from flask import Blueprint

mypage = Blueprint('mypage',__name__,template_folder='../templates')

from .errors import *

from .home import *
from .blog import *
from .media import *
from .console import *
from .login import *
from .service import *
from .siteinfo import *
from .api import *

from .middleware import *
#from .develop import *
