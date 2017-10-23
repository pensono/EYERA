from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lookup', views.get, name='index'),
    url(r'^$', views.index, name='index'),
]