# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import plan

# def OpenFormLogin(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/dashboard')
#     else:
#         # Return an 'invalid login' error message.
# 		context = { login_error = "true" }
# 	return render(request, 'login.html')

def index(request):
	return redirect('/accounts/login')

@login_required
def dashboard(request):
	return render(request, 'dashboard.html')

def plans(request):
	plan_data = plan.objects.all()


	context = {
		'title':'Plans',
		'activeplanes':'active',
		'plan_data': plan_data
		}
	return render(request, 'plans.html', context)

def new_plan(request):
	context = {
		'title':'Plans',
		# 'activenewplan':'active',
		'activenewplan':'current',
		}
	step=request.session.get('step', '1')

	if step == '1':
		request.session['step']='2'
		return render(request, 'new_plan.html', context)
	if step == '2':
		request.session['step']='3'
		return render(request, 'new_plan.html', context)
	if step == '3':
		request.session['step']='4'
		return render(request, 'new_plan.html', context)
	if step == '4':
		request.session['step']='1'
		return render(request, 'new_plan.html', context)
	if int(step) > 4:
		return render(request, 'new_plan.html', context)
