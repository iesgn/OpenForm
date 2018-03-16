# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from . import repository

def new_plan(request):
	context={}
	context["provider"]=request.POST['provider']
	return render(request, 'instance.html', context)

def _genplan(request):
	provider=request.POST['provider']
	request_data=repository.RequestRepo(request)
	instance_data=request_data._post_os_instances()
	instance=repository.Instances(provider)
	plan=instance.get_plan(instance_data)
	return showplan(request, plan)

def showplan(request, plan):
	context={}
	context["plan"]=plan
	return render(request, 'plan.html', context)
