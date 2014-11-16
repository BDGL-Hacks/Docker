from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^create/$', views.create_image, name='create'),
	url(r'^containers/$', views.display_instances, name='containers'),
	url(r'^containers/detail/$', views.container_details, name='container detail'),
	url(r'^images/$', views.display_images, name='images'),
	url(r'^images/detail/$', views.image_details, name='container detail'),
)
