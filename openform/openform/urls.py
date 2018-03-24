# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('gen/', include('generator.urls')),
]
