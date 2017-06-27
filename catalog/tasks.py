# -*- coding: utf-8 -*-
# @Author: lordofhogwarts
# @Date:   2017-06-27 10:20:50
# @Last Modified by:   lordofhogwarts
# @Last Modified time: 2017-06-27 15:36:34
from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Service, Layer
from owslib.wms import WebMapService
from celery import shared_task, Celery

#app= Celery('tasks',broker='amqp://localhost:8000//')
@shared_task
def create_layer(service_ID):
	URL= Service.objects.get(pk=service_ID).service_URL
	wms = WebMapService(URL)
	list1= list(wms.contents)
	layer_count= len(list1)
#	if created: 
	for i in range (layer_count):
		Service.objects.get(pk=service_ID).layer_set.create(layer_name=list1[i], layer_title=wms[list1[i]].title, layer_abstract=wms[list1[i]].abstract)
