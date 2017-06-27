# -*- coding: utf-8 -*-
# @Author: lordofhogwarts
# @Date:   2017-06-13 14:58:49
# @Last Modified by:   lordofhogwarts
# @Last Modified time: 2017-06-27 15:04:16
from __future__ import absolute_import, unicode_literals

from .celery_file import app as celery_app

__all__ = ['celery_app']

