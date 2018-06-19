# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import plan, provider, credential_type, OpenFormUser, credentials, aws_instance, aws_credential
from .forms  import OpenFormUserCreationForm, OpenFormProvidersForm, OpenFormCredentialTypeAWS, OpenFormCredentialTypeOS

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

def register(request):
	form = OpenFormUserCreationForm()
	return render(request, 'registration/register.html', {'form':form})

def _new_user(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		print('Method post!')
		form = OpenFormUserCreationForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			print('formulario valido!')
			form.save()
			username=request.POST['username']
			password=request.POST['password1']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/dashboard')
		else:
			print(form.errors)
			return redirect('/accounts/login/')
	else:
		return redirect('/accounts/login/')

@login_required
def dashboard(request):
	return render(request, 'dashboard.html')

def plans(request):
	plan_data = plan.objects
	# Limit of plans for user
	plan_limit = 5
	context = {
		'title':'Plans',
		'activeplanes':'active',
		'plan_data': plan_data.all(),
		'plan_count': plan_data.count(),
		'plan_limit': plan_limit
		}
	return render(request, 'plans.html', context)

def new_plan_providers(request):
	context = {
		# 'activenewplan':'active',
		'activenewplan':'current',
		}
	user=request.user.username
	print(user)
	# provider_id=request.GET['provider_id']
	context['provider'] = provider.objects.all()
	return render(request, 'new_plan_providers.html', context)

def new_plan_credentials(request):
	context = {}
	provider_id = request.GET['provider_id']
	provider_name = provider.objects.get(provider_id=provider_id).name
	context['provider_id'] = provider_id
	context['provider_name'] = provider_name
	# keys = credentials.objects.all()
	# for key in keys:
		# if key.username.username == user:
	# 		print(aws_credential.objects.get(id=key.credential_type_id.id).id)
			# context['credential_list'].append(credentials.objects.get(id=key.credential_type_id.id))
	# # keys.ge
	#
	credential_list=aws_credential.objects.filter()
	# # Must change this method
	if provider_id == '1':
		context['aws_form']=OpenFormCredentialTypeAWS()
	elif provider_id == '2':
		context['os_form']=OpenFormCredentialTypeOS()
	else:
		raise Http404("No provider found with that id.")
	print('Dentro del 2!')
	return render(request, 'new_plan_credentials.html', context)


def gen_plan(request):
	plan_name=request.GET['plan']
	context={}
	plan_id=plan.objects.get(name=plan_name).id
	context['plan_provider']=plan.objects.get(name=plan_name).provider_id.provider_id
	# 1 = AWS, must change this
	if context['plan_provider'] == '1':
		credential_id=plan.objects.get(name=plan_name).credential_id.id
		credential_type_id = credentials.objects.get(id=credential_id).credential_type_id.id
		context['aws_access_key'] = aws_credential.objects.get(id=credential_type_id).access_key
		context['aws_secret_key'] = aws_credential.objects.get(id=credential_type_id).secret_key
		context['instance_data'] = aws_instance.objects.filter(plan_id=plan_id)

	return render(request,'gen_plan.html', context)



def _new_credential(request):

	if request.method == 'POST':
		username=request.session.get('username')
		provider_id = request.POST['provider_id']
		print(provider_id)
		if provider_id == '1':
			form=OpenFormCredentialTypeAWS(request.POST)
			# check whether it's valid:
			if form.is_valid():
				print('formulario valido!')
				form.save()
				# Relation credential and user
				credential_name=request.POST['name']
				credential_type_id=credential_type.objects.get(name=credential_name).id
				credentials.objects.create(username=username,credential_type_id=credential_type_id)
				return redirect('/plans/new_plan/?step=2')
			else:
				print(form.errors)
		if provider_id == '2':
			form=OpenFormCredentialTypeOS(request.POST)
	else:
		if provider_id == '1':
			form=OpenFormCredentialTypeAWS()
		if provider_id == '2':
			form=OpenFormCredentialTypeOS()
