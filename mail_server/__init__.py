# -*- coding: utf-8 -*-
# Time: 2020-08-17 21:28
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py.py

from celery import Celery
from app.config import Config

"""
usage
celery -A mail_server worker -l info -f celery.log --pool=eventlet

"""
celery = Celery('mail_server',include=['mail_server.task1','mail_server.task2','mail_server.task4'])
celery.config_from_object("mail_server.celery_conf")

sender = Config.MAIL_USER
passwd = Config.MAIL_PW
host = Config.MAIL_HOST
port = Config.MAIL_PORT

