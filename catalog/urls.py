from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),

	url(r'^(?P<service_id>[0-9]+)/$',views.s_detail,name='detail'),

	url(r'^(?P<service_id>[0-9]+)/(?P<layer_id>[0-9]+)/$',views.layer,name='layer'),

]