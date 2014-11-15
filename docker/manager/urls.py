from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create_image, name='create'),
)
