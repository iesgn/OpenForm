from django.contrib import admin
from . import models
from . import forms

#
# class UsersAdmin(admin.ModelAdmin):
#     form = forms.UsersForm
#
# # admin.site.register(models.users)
# admin.site.register(models.users, UsersAdmin)

# class TransactionAdmin(admin.ModelAdmin):
#     form = TransactionForm
#
# admin.site.register(Transaction, TransactionAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from openform import models
 # OpenFormUser, provider, credentials, aws_credential, plan, instance, instance_image, network, flavor,aws_instance_type
from .forms import OpenFormUserChangeForm, OpenFormUserCreationForm, OpenFormProvidersForm,  OpenFormCredentialTypeAWS, OpenFormAWSInstance

class OpenFormUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    form = OpenFormUserChangeForm
    add_form = OpenFormUserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(models.OpenFormUser, OpenFormUserAdmin)
#
class OpenFormProviders(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ('name', 'description')})
#     ]
#     form = OpenFormProvidersForm
#     add_form = OpenFormProvidersForm
    search_fields = ('provider_id', 'name')
    list_display = ('name', 'description')

admin.site.register(models.provider, OpenFormProviders)

class OpenFormCredentials(admin.ModelAdmin):
    list_display = ('username', 'credential_type_id')

admin.site.register(models.credentials, OpenFormCredentials)

class OpenFormPlan(admin.ModelAdmin):
    list_display = ('name', 'username')

admin.site.register(models.plan, OpenFormPlan)

class OpenFormAWSCredentials(admin.ModelAdmin):
    list_display = ('name', 'access_key')
    form = OpenFormCredentialTypeAWS

admin.site.register(models.aws_credential, OpenFormAWSCredentials)

class OpenFormAWSInstance(admin.ModelAdmin):
    list_display = ('name', 'ami_id')
    form = OpenFormAWSInstance

admin.site.register(models.aws_instance, OpenFormAWSInstance)

class OpenFormAWSAmi(admin.ModelAdmin):
    list_display = ('name', 'ami_id')

admin.site.register(models.aws_ami, OpenFormAWSAmi)


class OpenFormAWSVpc(admin.ModelAdmin):
    list_display = ('name', 'vpc_id')

admin.site.register(models.aws_vpc,OpenFormAWSVpc)

class OpenFormAWSInstanceType(admin.ModelAdmin):
    list_display = ('name', 'instance_type_id')

admin.site.register(models.aws_instance_type,OpenFormAWSInstanceType)
