from django.shortcuts import render
from django.conf.urls import url, include

from . import views[
    url('gallery', views.gallery, name='gallery'),
    ulr('feedback/', views.addFeedback, name='feedback'),
]
