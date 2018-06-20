# -*- coding: utf-8 -*-

from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/register/new_user', views._new_user, name='new_user'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('plans/', views.plans, name='plans'),
    path('plans/instances', views.plan_instances, name='plan_instances'),
    path('plans/create', views.create_plan, name='create_plan'),
    path('plans/new_plan/', views._new_plan, name='new_plan'),
    path('plans/new_plan/providers', views.new_plan_providers, name='new_plan_providers'),
    path('plans/new_plan/credentials', views.new_plan_credentials, name='new_plan_credentials'),
    path('plans/new_plan/ami', views.new_plan_ami, name='new_plan_ami'),
    path('plans/new_plan/flavor', views.new_plan_flavor, name='new_plan_flavor'),
    path('plans/new_plan/instance', views.new_plan_instance, name='new_plan_instance'),
    path('plans/gen_plan/', views.gen_plan, name='gen_plan'),

    path('instances/new_instance/', views._new_instance, name='new_instance'),
    path('credentials/new_credential/', views._new_credential, name='new_credential'),
    path('images/new_image/', views._new_image, name='new_image'),
    path('flavors/new_flavor/', views._new_flavor, name='new_flavor'),
    path('instances/', views.list_instances, name='list_instance'),
    path('credentials/', views.list_credentials, name='list_credentials'),
    path('images/', views.list_images, name='list_images'),
    path('flavors/', views.list_flavors, name='list_flavors'),
    # path('gen/', include('generator.urls')),
]
