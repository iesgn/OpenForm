# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# USER models
class users(models.Model):
    # user_id = models.CharField(max_length=50, primary_key=True) # autoincrement
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class credential_type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class credentials(models.Model):
    user_id = models.ForeignKey(users,
        on_delete=models.CASCADE)
    credential_type_id = models.ForeignKey(credential_type,
        on_delete=models.CASCADE)

# PLAN models

class plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    user_name = models.ForeignKey(users,
        on_delete=models.CASCADE)
    credential_id = models.ForeignKey(credentials,
        on_delete=models.CASCADE)

# INSTANCE models

class instances(models.Model):
    plan_id = models.ForeignKey(plan,
        on_delete=models.CASCADE)

# SECURITY GROUPS models

class security_groups(models.Model):
    plan_id = models.ForeignKey(plan,
        on_delete=models.CASCADE)

class plan_sg(models.Model):
    plan_id = models.ForeignKey(plan,
        on_delete=models.CASCADE)
    sg_id = models.ForeignKey(security_groups,
        on_delete=models.CASCADE)
    instance_id = models.ForeignKey(instances,
        on_delete=models.CASCADE)




#############
# AWS models #
#############
# class aws_instances(instances):
#     key_name = models.CharField(max_length=50)
#     ami_id =  models.ForeignKey(aws_ami,
#         on_delete=models.CASCADE)
#     instance_type = models.ForeignKey(aws_flavor,
#         on_delete=models.CASCADE)

class credential_aws(credential_type):
    access_key = models.CharField(max_length=50)
    secret_key = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

#############
# OS models #
#############

class credential_os(credential_type):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cert_file = models.CharField(max_length=50) # type file, get $pwd/file (file path)
    tenant_name = models.CharField(max_length=50)
