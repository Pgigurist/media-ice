from django.shortcuts import render
from django.conf.urls import url, include

from . import views
urlpatterns = [
    url(r'^/$', views.list, name='list'),
    url(r'^/(?P<event_id>[0-9])/$', views.event, name='event'),
]
