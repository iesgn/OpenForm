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

from .models import OpenFormUser, provider
from .forms import OpenFormUserChangeForm, OpenFormUserCreationForm, OpenFormProvidersForm

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

admin.site.register(OpenFormUser, OpenFormUserAdmin)

class OpenFormProviders(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'description')})
    ]
    form = OpenFormProvidersForm
    add_form = OpenFormProvidersForm
    list_display = ('name', 'description')

admin.site.register(provider, OpenFormProviders)
