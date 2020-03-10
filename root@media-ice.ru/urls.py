from django.shortcuts import render
from django.conf.urls import url, include

from . import views
urlpatterns = [
    url(r'^$', views.camps, name='camps'),
    url(r'^/(?P<camp_id>[0-9])/$', views.camp, name='camp'),
] 
