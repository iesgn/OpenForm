# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

def _genplan(request):
    instance_name=request.POST['instance_name']
    instance_image_id=request.POST['instance_image_id']
    instance_flavor_id=request.POST['instance_flavor_id']
    instance_key_pair=request.POST['instance_key_pair']
    instance_security_groups=request.POST['instance_security_groups']


def showplan(request):

	return render(request, 'plan.html', json_data)
