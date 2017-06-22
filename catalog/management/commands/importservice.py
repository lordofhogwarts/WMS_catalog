from django.core.management.base import BaseCommand, CommandError
from catalog.models import Service, Layer
from owslib.wms import WebMapService

class Command(BaseCommand):
    help = 'Import services and load layers'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *arg, **options):
        for url in options['url']:
 #           try:
                # grab WebMapService and its layers
                wms = WebMapService(url)
                list1= list(wms.contents)
                layer_count= len(list1)
                service = Service(service_name=wms.identification.title, service_title=wms.identification.title, service_URL=wms.url)
                service.save()
                for i in range (layer_count):
                	service.layer_set.create(layer_name=list1[i], layer_title=wms[list1[i]].title, layer_abstract=wms[list1[i]].abstract)
  #          except:
