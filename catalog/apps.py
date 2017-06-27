# Author: Chuong Thao
# Date created: 6/15/2017
# Date last modified: 6/26/2017
# Python Version: 3.5

from django.apps import AppConfig
from django.db.models.signals import post_save

class CatalogConfig(AppConfig):
    name = 'catalog'
 #   verbose_name = _('catalog')

    def ready(self):
    	from catalog.signals import create_layer_signal