# -*- coding: utf-8 -*-
# Time: 2020-08-17 17:40
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: celery_conf.py

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_RESULT_EXPIRES = 60 * 2
CELERY_DISABLE_RATE_LIMITS = True
CELERY_TIMEZONE = 'Asia/Shanghai'

