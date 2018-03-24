# -*- coding: utf-8 -*-
import json
import uuid
# from . import models

class RequestRepo(object):
    def __init__(self, request):
        self.request=request
        self.os_instance_data=[]

    def _post_os_instances(self):
        # Aquí habrá que rellenar una lista con los datos de cada instancia.
        # Deberá llamar a una función por cada provedor.
        self._post_os_instances_names()
        self._post_os_instances_images()
        self._post_os_instances_flavors()
        self._post_os_instances_keypairs()
        self._post_os_instances_secgroups()
        return self.os_instance_data

    def _post_os_instances_names(self):
        names=self.request.POST.getlist('instance_name')
        self.os_instance_data.append(names)

    def _post_os_instances_images(self):
        images=self.request.POST.getlist('instance_image_id')
        self.os_instance_data.append(images)

    def _post_os_instances_flavors(self):
        flavors=self.request.POST.getlist('instance_flavor_id')
        self.os_instance_data.append(flavors)

    def _post_os_instances_keypairs(self):
        key_pairs=self.request.POST.getlist('instance_key_pair')
        self.os_instance_data.append(key_pairs)

    def _post_os_instances_secgroups(self):
        secgroups=self.request.POST.getlist('instance_security_groups')
        self.os_instance_data.append(secgroups)
#
# class Provider(object):
#     def get_name()


class Instances(object):
    def __init__(self, provider):
        self.provider=provider
        self.resource_name=str(uuid.uuid4())
        self.instance={}
        self.instances_plan=[]

    def _os_instance(self,instance_data):
        # resource_type se consultará a una base de datos
        self.resource_type="openstack_compute_instance_v2"
        for name, image, flavor, key_pair, secgroup in zip(instance_data[0],instance_data[1],instance_data[2],instance_data[3],instance_data[4]):
            self.instance[name]={'name': name,
                                'image_id': image,
                                'flavor_id': flavor,
                                'key_pair': key_pair,
                                'security_groups':secgroup}
        self.json_data=json.dumps(self.instance,indent=4)
        # print(self.json_data)

    def get_plan(self,instance_data):
        self._os_instance(instance_data)
        # plan_data=self.json_data
        for i in self.instance.keys():
            self.instances_plan.append(json.dumps(
            {
                "resource": {
                    self.resource_type:
                        self.instance[i]
                        }
            }, indent=4))
        return self.instances_plan
