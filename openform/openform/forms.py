from django import forms
from django.forms import ModelForm
# from . import models


# class UsersForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = models.users
#         fields = "__all__"

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import OpenFormUser, provider, aws_credential, os_credential, aws_instance, aws_ami, aws_instance_type, plan,os_instance

class OpenFormUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    # def __init__(self, *args, **kargs):
    #     super(OpenFormUserCreationForm, self).__init__(*args, **kargs)
    #     del self.fields['username']
    class Meta:
        model = OpenFormUser
        fields = ("username", "email")

class OpenFormUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta:
        model = OpenFormUser
        fields = "__all__"

    # def __init__(self, *args, **kargs):
    #     super(OpenFormUserChangeForm, self).__init__(*args, **kargs)
    #     del self.fields['username']

class OpenFormProvidersForm(ModelForm):
    class Meta:
        model = provider
        fields = "__all__"

class OpenFormPlanForm(ModelForm):
    class Meta:
        model = plan
        fields = "__all__"


class OpenFormCredentialTypeAWS(ModelForm):
    secret_key = forms.CharField(widget=forms.PasswordInput())
    # provider_id = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = aws_credential
        fields = "__all__"

class OpenFormCredentialTypeOS(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # provider_id = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = os_credential
        fields = "__all__"

class OpenFormAWSInstance(ModelForm):
    key_name = forms.CharField(help_text='Absolute path to the ssh key. Ej: /home/user/.ssh/project.pem')
    # provider_id = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = aws_instance
        fields = "__all__"

class OpenFormOSInstance(ModelForm):
    class Meta:
        model = os_instance
        fields = "__all__"


class OpenFormAmiAWS(ModelForm):
    class Meta:
        model = aws_ami
        fields = "__all__"


class OpenFormAWSFlavor(ModelForm):
    class Meta:
        model = aws_instance_type
        fields = "__all__"
