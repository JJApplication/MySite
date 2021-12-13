# -*- coding: utf-8 -*-
# Time: 2020-08-02 19:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: conf.py

#配置文件
import os
from datetime import timedelta
class Config:
    SECRET_KEY = 'landers1037-renj.io'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'app', 'data.db')
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(hours=1)
    TESTING = False
    MAX_CONTENT_LENGTH = 3 *1024 * 1024
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = False
    MAX_VIEW_EXPIRES =  60 * 5

    MAIL_HOST = 'mail.gandi.net'
    MAIL_PORT = 465
    MAIL_USER = 'bot@renj.io'
    MAIL_PW = '19980514mail'

    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_TASK_RESULT_EXPIRES = 60 * 2
    CELERY_DISABLE_RATE_LIMITS = True
    CELERY_TIMEZONE = 'Asia/Shanghai'

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'data.sqlite')

class DevelopConfig(Config):
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=5)
    TESTING = True
    DEBUG = True
