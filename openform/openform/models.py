# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django import forms
# from django.contrib.auth.models import User
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

# Custom Auth models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class OpenFormUserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class OpenFormUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('username'), max_length=50, unique=True)
    email = models.EmailField(_('Email'), max_length=254, unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('Administrador'), default=False,
        help_text=_('Indica si el usuario podrá acceder a la zona de administración'))
    is_active = models.BooleanField(_('Active'), default=True,
        help_text=_('Indica si la cuenta del usuario está activa. '
                    'Desmarca esta opción en vez de eliminar cuentas.'))
    date_joined = models.DateTimeField(_('Fecha de alta'), default=timezone.now)

    objects = OpenFormUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])



# class Profile(models.Model):
#     username = models.OneToOneField(OpenFormUser, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

# USER models
# class users(models.Model):
#     # user_id = models.CharField(max_length=50, primary_key=True) # autoincrement
#     user_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)


# Provider models

class provider(models.Model):
    provider_id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

# Credentials models

class credential_type(models.Model):
    """
    Common cretentials type fields.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)


class credentials(models.Model):
    """
    List of users credentials.
    """
    username = models.ForeignKey(OpenFormUser,
        on_delete=models.CASCADE)
    credential_type_id = models.ForeignKey(credential_type,
        on_delete=models.CASCADE)

# PLAN models

class plan(models.Model):
    """
    Plan fields.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    username = models.ForeignKey(OpenFormUser, on_delete=models.CASCADE)
    credential_id = models.ForeignKey(credentials,
        on_delete=models.CASCADE)


# INSTANCE models

class instance(models.Model):
    plan_id = models.ForeignKey(plan,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)

# SECURITY GROUPS models

class security_groups(models.Model):
    plan_id = models.ForeignKey(plan,
        on_delete=models.CASCADE)

class plan_sg(models.Model):
    plan_id = models.ForeignKey(plan,
        on_delete=models.CASCADE)
    sg_id = models.ForeignKey(security_groups,
        on_delete=models.CASCADE)
    instance_id = models.ForeignKey(instance,
        on_delete=models.CASCADE)

# IMAGES models

class instance_image(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)

# NETWORKS models

class network(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)

# FLAVORS models

class flavor(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)

##############
# AWS models #
##############
class aws_instance_type(flavor):
    instance_type_id = models.CharField(max_length=50)

class aws_vpc(network):
    vpc_id = models.CharField(max_length=50)

class aws_ami(instance_image):
    ami_id = models.CharField(max_length=50)

class aws_instance(instance):
    key_name = models.CharField(max_length=50)
    ami_id =  models.ForeignKey(aws_ami,
        on_delete=models.CASCADE)
    instance_type_id = models.ForeignKey(aws_instance_type,
        on_delete=models.CASCADE)

class aws_credential(credential_type):
    access_key = models.CharField(max_length=50)
    secret_key = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

# data = {'access_key':'test' ,'secret_key':'test','region':'test','name':'test','description':'test'}
#############
# OS models #
#############

class os_flavor(flavor):
    flavor_id = models.CharField(max_length=50)

class os_network(network):
    network_id = models.CharField(max_length=50)

class os_image(instance_image):
    image_id = models.CharField(max_length=50)

class os_credential(credential_type):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cert_file = models.CharField(max_length=50) # type file, get $pwd/file (file path)
    tenant_name = models.CharField(max_length=50)

class os_instance(instance):
    key_pair = models.CharField(max_length=50)
    image_id =  models.ForeignKey(os_image,
        on_delete=models.CASCADE)
    flavor_id = models.ForeignKey(os_flavor,
        on_delete=models.CASCADE)
