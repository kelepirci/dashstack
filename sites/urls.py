from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='sites-index'),
    url(r'^list/$', views.sites_list, name='sites-list'),
]