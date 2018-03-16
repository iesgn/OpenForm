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
	instance_plan={}
	instance_plan["instance_name"]=request.POST['instance_name']
	instance_plan["instance_image_id"]=request.POST['instance_image_id']
	instance_plan["instance_flavor_id"]=request.POST['instance_flavor_id']
	instance_plan["instance_key_pair"]=request.POST['instance_key_pair']
	instance_plan["instance_security_groups"]=request.POST['instance_security_groups']
	instance=repository.Instances(provider)
	plan=instance.get_plan(instance_plan)
	return showplan(request, plan)

def showplan(request, plan):
	context={}
	context["plan"]=plan
	return render(request, 'plan.html', context)
