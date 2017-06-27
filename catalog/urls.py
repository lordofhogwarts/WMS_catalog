# Author: Chuong Thao
# Date created: 6/15/2017
# Date last modified: 6/26/2017
# Python Version: 3.5 

from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),

	url(r'^(?P<service_id>[0-9]+)/$',views.s_detail,name='detail'),

	url(r'^(?P<service_id>[0-9]+)/(?P<layer_id>[0-9]+)/$',views.layer,name='layer'),

]