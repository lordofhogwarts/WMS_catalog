from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),

	url(r'^$',views.s_detail,name='detail'),

	url(r'^$',views.layer,name='layer')
]