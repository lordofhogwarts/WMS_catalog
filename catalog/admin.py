from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
	fields= ['service_URL']

admin.site.register(Service)
