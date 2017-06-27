# -*- coding: utf-8 -*-
# @Author: Charles Thao
# @Date:   2017-06-27 09:28:21
# @Last Modified by:   lordofhogwarts
# @Last Modified time: 2017-06-27 15:33:28
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

#settings for Django module

os.environ.setdefault('DJANGO_SETTINGS_MODULE','WMS_catalog.settings')

app = Celery('WMS_catalog',backend='amqp', broker='amqp://guest@localhost//',
                include=['catalog.tasks'])

app.config_from_object('django.conf:settings',namespace= 'CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print('Request:{0!r}'.format(self.request))