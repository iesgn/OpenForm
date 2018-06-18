from django import forms
from django.forms import ModelForm
# from . import models


# class UsersForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = models.users
#         fields = "__all__"

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import OpenFormUser, provider

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
        fields = ("username", "email", "password")

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
