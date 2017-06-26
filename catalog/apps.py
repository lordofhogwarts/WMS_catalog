
from django.apps import AppConfig
from django.db.models.signals import post_save

class CatalogConfig(AppConfig):
    name = 'catalog'
 #   verbose_name = _('catalog')

    def ready(self):
    	from catalog.signals import create_layer