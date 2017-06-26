from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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

def s_detail(request,service_id):\
	service = get_object_or_404(Service, pk=service_id)
	return render(request,'catalog/detail.html',{'service':service})

def layer(request,service_id,layer_id):
	layer = get_object_or_404(Layer,pk=layer_id)
	context= {'layer':layer}
	return render(request,'catalog/layer.html',context)