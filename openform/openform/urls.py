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
    path('plans/new_plan/', views.new_plan, name='new_plan'),
    path('plans/new_credential/', views._new_credential, name='new_credential'),
    path('plans/gen_plan/', views.gen_plan, name='gen_plan'),
    # path('gen/', include('generator.urls')),
]
