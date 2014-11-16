from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^containers/$', views.display_instances, name='containers'),
	url(r'^containers/detail/$', views.container_details, name='container detail'),
	url(r'^containers/create/$', views.create_container, name='create container'),
	url(r'^images/$', views.display_images, name='images'),
	url(r'^images/detail/$', views.image_details, name='container detail'),
	url(r'^images/create/$', views.create_image, name='create image'),
)
