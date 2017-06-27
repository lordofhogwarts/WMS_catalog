# Author: Chuong Thao
# Date created: 6/15/2017
# Date last modified: 6/26/2017
# Python Version: 3.5


from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.models import Service, Layer
from celery import shared_task
from catalog.tasks import create_layer

'''
@receiver(post_save,sender= Service)
def create_layer(sender,instance,created,**kwargs):
	wms = WebMapService(instance.service_URL)
	list1= list(wms.contents)
	layer_count= len(list1)
	if created: 
		for i in range (layer_count):
			instance.layer_set.create(layer_name=list1[i], layer_title=wms[list1[i]].title, layer_abstract=wms[list1[i]].abstract)
'''

@receiver(post_save,sender= Service)
def create_layer_signal(sender,instance,created,**kwargs):
	if created:
		create_layer.delay(instance.id)