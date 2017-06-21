from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Service, Layer		
from django.template import loader
# Create your views here.
def index(request):
	service_list = Service.objects.all()
#	template = loader.get_template('catalog/index.html')
	context = {
	 'service_list' : service_list,
	}
	return render(request,'catalog/index.html',context)

def s_detail(request,service_id):
	service = Service.objects.get(pk=service_id)
	context= {'service':service}
	return render(request,'catalog/detail.html',context)

def layer(request,service_id,layer_id):
	layer = Layer.objects.get(pk=layer_id)
	context= {'layer':layer}
	return render(request,'catalog/layer.html',context)
	