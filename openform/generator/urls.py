# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('new_plan', views.new_plan, name="new_plan"),
    path('new_instance_plan', views.new_instance_plan, name="new_instance_plan"),
    path('new_network_plan', views.new_network_plan, name="new_network_plan"),
    path('_genplan', views._genplan, name="_genplan"),
]
