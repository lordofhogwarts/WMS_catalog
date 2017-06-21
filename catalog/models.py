from django.db import models

# Create your models here.
class Service(models.Model):
	service_name = models.CharField(max_length=200)
	service_title = models.CharField(max_length=200)
	service_URL = models.CharField(max_length=200)
	def __str__(self):
		return self.service_title

class Layer(models.Model):
	service = models.ForeignKey(Service,on_delete = models.CASCADE)	
	layer_name = models.CharField(max_length=200)
	layer_title = models.CharField(max_length=200)
	layer_abstract = models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.layer_title
