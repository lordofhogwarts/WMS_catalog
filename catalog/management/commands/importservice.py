# Author: Chuong Thao
# Date created: 6/15/2017
# Date last modified: 6/26/2017
# Python Version: 3.5

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
  #          except:
