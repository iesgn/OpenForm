# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from . import repository

def new_instance_plan(request):
	context={}
	context["provider"]=request.POST['provider']
	return render(request, 'instance.html', context)

def new_plan(request):
	context={}
	context["provider"]=request.POST['provider']
	context["resource_type"]=request.POST['resource_type']
	if context["resource_type"] == "Instancia":
		return render(request, 'instance.html', context)
	elif context["resource_type"] == "Red":
		return render(request, 'network.html', context)

def new_network_plan(request):
	context={}
	context["provider"]=request.POST['provider']
	return render(request, 'network.html', context)

def _genplan(request):
	# TODO: check resource type, by a external function
	provider=request.POST['provider']
	resource_type=request.POST['resource_type']
	request_data=repository.RequestRepo(request)
	if resource_type == "Instancia":
		instance_data=request_data._post_os_instances()
		instance=repository.Instances(provider)
		plan=instance.get_plan(instance_data)
	elif resource_type == "Red":
		network_data=request_data._post_os_network()
		network=repository.Networks(provider)
		plan=network.get_plan(network_data)

	return showplan(request, plan)

def showplan(request, plan):
	context={}
	context["plan"]=plan
	return render(request, 'plan.html', context)
