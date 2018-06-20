# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import plan, provider, credential_type, OpenFormUser, aws_instance, aws_credential, aws_ami, aws_instance_type, os_instance, os_credential, os_image, os_credential, os_flavor
from .forms  import OpenFormUserCreationForm, OpenFormProvidersForm, OpenFormCredentialTypeAWS, OpenFormCredentialTypeOS, OpenFormAmiAWS, OpenFormAWSInstance, OpenFormAWSFlavor, OpenFormPlanForm, OpenFormOSInstance

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
	try:
		request.user.is_autenticated()
		return redirect('/dashboard')
	except:
		return redirect('/accounts/login')


def register(request):
	form = OpenFormUserCreationForm()
	return render(request, 'registration/register.html', {'form':form})

@login_required
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

@login_required
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

@login_required
def new_plan_providers(request):
	context = {
		# 'activenewplan':'active',
		'activenewplan':'current',
		}
	context['provider'] = provider.objects.all()
	return render(request, 'new_plan_providers.html', context)

@login_required
def new_plan_credentials(request):
	username=OpenFormUser.objects.get(username=request.user.username)
	context = {}
	provider_id = request.GET['provider_id']
	provider_name = provider.objects.get(provider_id=provider_id).name
	context['provider_id'] = provider_id
	context['provider_name'] = provider_name

	# # Must change this method
	if provider_id == '1':
		context['aws_form']=OpenFormCredentialTypeAWS()
		try:
			context['aws_credential_list']=aws_credential.objects.filter(username=username)
		except:
			pass
	elif provider_id == '2':
		context['os_form']=OpenFormCredentialTypeOS()
		try:
			context['os_credential_list']=os_credential.objects.filter(username=username)
		except:
			pass
	else:
		raise Http404("No provider found with that id.")
	return render(request, 'new_plan_credentials.html', context)

@login_required
def new_plan_ami(request):
	context = {}
	provider_id = request.GET['provider_id']
	provider_name = provider.objects.get(provider_id=provider_id).name
	context['provider_id'] = provider_id
	context['provider_name'] = provider_name
	if provider_id == '1':
		context['aws_form']=OpenFormAmiAWS()
		try:
			context['aws_ami_list']=aws_ami.objects.filter(provider_id=provider_id)
		except:
			pass
	elif provider_id == '2':
		context['os_form']=OpenFormCredentialTypeOS()
		try:
			context['os_image_list']=os_images.objects.filter(provider_id=provider_id)
		except:
			pass

	return render(request, 'new_plan_ami.html', context)


@login_required
def new_plan_flavor(request):
	context = {}
	provider_id = request.GET['provider_id']
	provider_name = provider.objects.get(provider_id=provider_id).name
	context['provider_id'] = provider_id
	context['provider_name'] = provider_name
	if provider_id == '1':
		context['aws_form']=OpenFormAWSFlavor()
		try:
			context['aws_flavors_list']=aws_instance_type.objects.filter(provider_id=provider_id)
		except:
			pass
	elif provider_id == '2':
		context['os_form']=OpenFormCredentialTypeOS()
		try:
			context['os_image_list']=os_images.objects.filter(provider_id=provider_id)
		except:
			pass

	return render(request, 'new_plan_flavor.html', context)

@login_required
def create_plan(request):
	context = {}
	username=OpenFormUser.objects.get(username=request.user.username)
	get_provider_id = request.GET['provider_id']
	get_credential_type_id = request.GET['credential_type_id']
	provider_data = provider.objects.get(provider_id=get_provider_id)
	if provider_data.provider_id == 1:
		credential_type_id=aws_credential.objects.get(id=get_credential_type_id)
	if provider_data.provider_id == 2:
		credential_type_id=os_credential.objects.get(id=get_credential_type_id)

	context['provider_data'] = provider_data
	context['form']=OpenFormPlanForm(initial={'username':username,
		'provider_id':provider_data.provider_id,
		'credential_type_id':credential_type_id})
	return render(request, 'new_plan.html', context)


@login_required
def new_plan_instance(request):
	context = {}

	provider_id = request.GET['provider_id']
	provider_name = provider.objects.get(provider_id=provider_id).name
	context['provider_id'] = provider_id
	context['provider_name'] = provider_name
	if provider_id == '1':
		context['aws_form']=OpenFormAWSInstance()
		try:
			plan_id=request.session.get('plan_id_new')
			context['aws_instances_list']=aws_instance.objects.filter(plan_id=plan_id)
		except:
			pass
	elif provider_id == '2':
		context['os_form']=OpenFormCredentialTypeOS()
		try:
			plan_id=request.session.get('plan_id_new')
			context['os_image_list']=os_instance.objects.filter(plan_id=plan_id)
		except:
			pass

	return render(request, 'new_plan_instance.html', context)


def plan_instances(request):
	context={}
	# try:
	# 	if request.session.get('plan_id') is not None:
	# 		plan_id=request.session.get('plan_id')
	# except:
	try:
		del request.session['plan_id']
	except:
		print(request.session.get('plan_id'))
	request.session['plan_id']=request.GET['plan_id']
	plan_id=request.session.get('plan_id')
	provider_id=plan.objects.get(id=plan_id).provider_id.provider_id
	provider_name=provider.objects.get(provider_id=provider_id).name
	print(provider_name)
	print(provider_id)
	print(plan_id)
	context['provider_id'] = provider_id
	context['provider_name'] = provider_name
	context['aws_instances_list']=aws_instance.objects.filter(plan_id=plan_id)
	context['aws_form'] = OpenFormAWSInstance()
	context['os_instances_list']=os_instance.objects.filter(plan_id=plan_id)
	context['os_form'] = OpenFormOSInstance()
	return render(request, 'plan_instances.html', context)


@login_required
def gen_plan(request):
	plan_id=request.session.get('plan_id')
	context={}
	# plan_id=plan.objects.get(name=plan_name).id
	print(plan_id)
	context['plan_provider']=plan.objects.get(id=plan_id).provider_id.provider_id
	print(context['plan_provider'])
	# 1 = AWS, must change this
	if context['plan_provider'] == 1:
		print('Hola')
		credential_type_id=plan.objects.get(id=plan_id).credential_type_id.id
		# credential_type_id = credentials.objects.get(id=credential_id).credential_type_id.id
		context['aws_access_key'] = aws_credential.objects.get(id=credential_type_id).access_key
		context['aws_secret_key'] = aws_credential.objects.get(id=credential_type_id).secret_key
		context['instance_data'] = aws_instance.objects.filter(plan_id=plan_id)
	if context['plan_provider'] == 2:
		print('Hola')
		credential_type_id=plan.objects.get(id=plan_id).credential_type_id.id
		# credential_type_id = credentials.objects.get(id=credential_id).credential_type_id.id
		context['os_user_name'] = os_credential.objects.get(id=credential_type_id).user_name
		context['os_password'] = os_credential.objects.get(id=credential_type_id).password
		context['os_tenant_name'] = os_credential.objects.get(id=credential_type_id).tenant_name
		context['os_cert_file'] = os_credential.objects.get(id=credential_type_id).cert_file
		context['instance_data'] = os_instance.objects.filter(plan_id=plan_id)



	return render(request,'gen_plan.html', context)


@login_required
def _new_plan(request):
	if request.method == 'POST':
		username=OpenFormUser.objects.get(username=request.user.username)
		provider_id = request.POST['provider_id']
		credential_type_id = request.POST['credential_type_id']
		print(provider_id)
		if provider_id == '1':
			form=OpenFormPlanForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				form.save()
				request.session.flush()
				plan_id=plan.objects.get(name=request.POST['name']).id
				print(plan_id)
				request.session['plan_id']=plan_id
				return redirect('/plans/new_plan/ami?provider_id=%s' %(provider_id))
			else:
				print(form.errors)
	return redirect('/plans/create_plan?credential_type_id=%s' %(credential_type_id))


@login_required
def _new_image(request):

	if request.method == 'POST':
		username=OpenFormUser.objects.get(username=request.user.username)
		provider_id = request.POST['provider_id']
		print(provider_id)
		if provider_id == '1':
			form=OpenFormAmiAWS(request.POST)
			# check whether it's valid:
			if form.is_valid():
				print('formulario valido!')
				form.save()
				return redirect('/plans/new_plan/image?provider_id=%s' %(provider_id))
			else:
				print(form.errors)
		if provider_id == '2':
			form=OpenFormCredentialTypeOS(request.POST)
	else:
		if provider_id == '1':
			form=OpenFormCredentialTypeAWS()
		if provider_id == '2':
			form=OpenFormCredentialTypeOS()
	return redirect('/plans/new_plan/providers')

@login_required
def _new_credential(request):

	if request.method == 'POST':
		username=OpenFormUser.objects.get(username=request.user.username)
		provider_id = request.POST['provider_id']
		print(provider_id)
		if provider_id == '1':
			form=OpenFormCredentialTypeAWS(request.POST)
			# check whether it's valid:
			if form.is_valid():
				print('formulario valido!')
				form.save()
				return redirect('/plans/new_plan/credentials?provider_id=%s' %(provider_id))
			else:
				print(form.errors)
		if provider_id == '2':
			form=OpenFormCredentialTypeOS(request.POST)
	else:
		if provider_id == '1':
			form=OpenFormCredentialTypeAWS()
		if provider_id == '2':
			form=OpenFormCredentialTypeOS()
	return redirect('/plans/new_plan/providers')

@login_required
def _new_instance(request):

	plan_id = request.session.get('plan_id')
	if request.method == 'POST':
		username=OpenFormUser.objects.get(username=request.user.username)
		provider_id = request.POST['provider_id']
		print(provider_id)
		if provider_id == '1':
			form=OpenFormAWSInstance(request.POST)
			# check whether it's valid:
			if form.is_valid():
				print('formulario valido!')
				form.save()
				return redirect('/plans/instances?plan_id=%s' %(plan_id))
			else:
				print(form.errors)
		if provider_id == '2':
			form=OpenFormOSInstance(request.POST)
			# check whether it's valid:
			if form.is_valid():
				print('formulario valido!')
				form.save()
				return redirect('/plans/instances?plan_id=%s' %(plan_id))
			else:
				print(form.errors)
	else:
		if provider_id == '1':
			form=OpenFormAWSInstance()
		if provider_id == '2':
			form=OpenFormCredentialTypeOS()
	return redirect('/plans/new_plan/providers')

@login_required
def _new_flavor(request):
	if request.method == 'POST':
		provider_id = request.POST['provider_id']
		print(provider_id)
		if provider_id == '1':
			form=OpenFormAWSFlavor(request.POST)
			# check whether it's valid:
			if form.is_valid():
				form.save()
				return redirect('/plans/create?provider_id=%s' %(provider_id))
			else:
				print(form.errors)
		if provider_id == '2':
			form=OpenFormCredentialTypeOS(request.POST)
	else:
		if provider_id == '1':
			form=OpenFormAWSFlavor()
		if provider_id == '2':
			form=OpenFormCredentialTypeOS()
	return redirect('/plans/new_plan_providers')


@login_required
def list_credentials(request):
	context = {}
	username=OpenFormUser.objects.get(username=request.user.username)
	context['providers']=provider.objects.all()
	print(username)
	context['credential_aws_list'] = aws_credential.objects.all()
	context['credential_os_list'] = os_credential.objects.all()
	# context['credential_os_list'] = os_credential.objects.all()


	return render(request, 'credentials.html', context)


@login_required
def list_instances(request):
	context = {}
	username=OpenFormUser.objects.get(username=request.user.username)
	context['providers']=provider.objects.all()
	context['instances_aws_list'] = aws_instance.objects.all()
	return render(request, 'instances.html', context)

@login_required
def list_images(request):
	context = {}
	username=OpenFormUser.objects.get(username=request.user.username)
	context['providers']=provider.objects.all()
	print(username)
	context['images_aws_list'] = aws_ami.objects.all()
	context['images_os_list'] = os_image.objects.all()

	# context['credential_os_list'] = os_credential.objects.all()
	return render(request, 'os_images.html', context)

@login_required
def list_flavors(request):
	context = {}
	username=OpenFormUser.objects.get(username=request.user.username)
	context['providers']=provider.objects.all()
	context['flavors_aws_list'] = aws_instance_type.objects.all()
	context['flavors_os_list'] = os_flavor.objects.all()
	# context['credential_os_list'] = os_credential.objects.all()
	return render(request, 'flavors.html', context)


@login_required
def update_credentials(request):
	context = {}
	username=OpenFormUser.objects.get(username=request.user.username)
	print(username)
	context['credential_aws_list'] = aws_credential.objects.all()
	# context['credential_os_list'] = os_credential.objects.all()


	return render(request, 'credentials.html', context)
