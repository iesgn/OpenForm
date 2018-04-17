# -*- coding: utf-8 -*-
import json
import uuid
# from . import models

class RequestRepo(object):
    def __init__(self, request):
        self.request=request
        self.os_instance_data=[]
        self.os_network_data=[]
        self.os_volume_data=[]

    # Volume request
    def _post_os_volume(self):
        # Aquí habrá que rellenar una lista con los datos de cada instancia.
        # Deberá llamar a una función por cada provedor.
        self._post_os_volume_name()
        self._post_os_volume_size()
        self._post_os_volume_desc()
        return self.os_volume_data

    def _post_os_volume_name(self):
        names=self.request.POST.getlist('volume_name')
        self.os_volume_data.append(names)

    def _post_os_volume_size(self):
        size=self.request.POST.getlist('volume_size')
        self.os_volume_data.append(size)

    def _post_os_volume_desc(self):
        desc=self.request.POST.getlist('volume_desc')
        self.os_volume_data.append(desc)

    # Nework request
    def _post_os_network(self):
        # Aquí habrá que rellenar una lista con los datos de cada instancia.
        # Deberá llamar a una función por cada provedor.
        self._post_os_network_name()
        self._post_os_network_cidr()
        return self.os_network_data

    def _post_os_network_name(self):
        names=self.request.POST.getlist('network_name')
        self.os_network_data.append(names)

    def _post_os_network_cidr(self):
        cidr=self.request.POST.getlist('network_cidr')
        self.os_network_data.append(cidr)

    # Instance request
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
                    self.resource_type: {
                            self.instance[i]['name']: self.instance[i]
                    }
                }
            }, indent=4))
        return self.instances_plan

class Networks(object):
    def __init__(self, provider):
        self.provider=provider
        self.resource_name=str(uuid.uuid4())
        self.network={}
        self.subnet={}
        self.networks_plan=[]

    def _os_network(self,network_data):
        # resource_type se consultará a una base de datos
        self.network_resource_type="openstack_networking_network_v2"
        for name in network_data[0]:
            self.network[name]={'name': name,
                                'admin_state_up': 'true'}
        # self.json_data=json.dumps(self.network,indent=4)

    def _os_subnet(self,network_data):
        # resource_type se consultará a una base de datos
        self.subnet_resource_type="openstack_networking_subnet_v2"
        for name, cidr in zip(network_data[0], network_data[1]):
            self.subnet[name]={ 'name': 'subnet-' + name,
                                # Need fix this
                                # 'network_id': "${openstack_networking_network_v2." + self.subnet[name] + ".id}",
                                'cidr': cidr}
        # self.json_data=json.dumps(self.network,indent=4)

    def get_plan(self,network_data):
        self._os_network(network_data)
        self._os_subnet(network_data)
        # plan_data=self.json_data
        for i in self.network.keys():
            self.networks_plan.append(json.dumps(
            {
                "resource": {
                    self.network_resource_type: {
                        self.network[i]['name']: self.network[i]
                    }
                }
            }, indent=4))
        for i in self.subnet.keys():
            self.networks_plan.append(json.dumps(
            {
                "resource": {
                    self.subnet_resource_type: {
                        self.subnet[i]['name']: self.subnet[i]
                    }
                }
            }, indent=4))
        return self.networks_plan
## Internal network
# resource "openstack_networking_network_v2" "interna-openstack" {
#   name           = "interna-openstack"
#   admin_state_up = "true"
# }
#
# resource "openstack_networking_subnet_v2" "subnet-openstack" {
#   name       = "subnet-openstack"
#   network_id = "${openstack_networking_network_v2.interna-openstack.id}"
#   cidr       = "192.168.200.0/24"
#   ip_version = 4
# }

class Volumes(object):
    def __init__(self, provider):
        self.provider=provider
        self.resource_name=str(uuid.uuid4())
        self.volume={}
        self.volumes_plan=[]

    def _os_volume(self,volume_data):
        # resource_type se consultará a una base de datos
        self.volume_resource_type="openstack_blockstorage_volume_v2"
        for name, size, desc in zip(volume_data[0],volume_data[1],volume_data[2]):
            self.volume[name]={'name': name,
                                'size': size,
                                'description': desc}

    def get_plan(self,volume_data):
        self._os_volume(volume_data)
        # plan_data=self.json_data
        for i in self.volume.keys():
            self.volumes_plan.append(json.dumps(
            {
                "resource": {
                    self.volume_resource_type: {
                            self.volume[i]['name']: self.volume[i]
                    }
                }
            }, indent=4))
        return self.volumes_plan
# create new volume, not attached
# resource "openstack_blockstorage_volume_v2" "terraform" {
#   name        = "openstack"
#   description = "Volume create by terraform"
#   size        = 5
# }
#
# # attach volume to orbit
# resource "openstack_compute_volume_attach_v2" "attachedtorobit" {
#   instance_id = "${openstack_compute_instance_v2.orbit.id}"
#   volume_id = "${openstack_blockstorage_volume_v2.terraform.id}"
# }
#
