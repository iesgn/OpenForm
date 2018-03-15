# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('new_plan', views.new_plan, name="new_plan"),
    path('_genplan', views._genplan, name="_genplan"),
]
