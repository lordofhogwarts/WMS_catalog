from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.models import Service, Layer
from owslib.wms import WebMapService

@receiver(post_save,sender= Service)
def create_layer(sender,instance,created,**kwargs):
	wms = WebMapService(instance.service_URL)
	list1= list(wms.contents)
	layer_count= len(list1)
	if created:
		for i in range (layer_count):
			instance.layer_set.create(layer_name=list1[i], layer_title=wms[list1[i]].title, layer_abstract=wms[list1[i]].abstract)
