# -*- coding: utf-8 -*-
import json
import uuid
# from . import models

class InstancesRepo(object):
    def __init__(self, provider):
        self.provider=provider
        self.resource_name=str(uuid.uuid4())

    def _os_instance(self,instance_plan):
        # resource_type se consultará a una base de datos
        self.resource_type="openstack_compute_instance_v2"
        self.instance_name=instance_plan["instance_name"]
        self.instance_image_id=instance_plan["instance_image_id"]
        self.instance_flavor_id=instance_plan["instance_flavor_id"]
        self.instance_key_pair=instance_plan["instance_key_pair"]
        self.instance_security_groups=[instance_plan["instance_security_groups"]]

    def get_plan(self,instance_plan):
        self._os_instance(instance_plan)
        plan_data=json.dumps(
            {
            "resource": {
                self.resource_type: {
                    self.resource_name: {
                        "name": self.instance_name,
                        "image_id": self.instance_image_id,
                        "flavor_id": self.instance_flavor_id,
                        "key_pair": self.instance_key_pair,
                        "security_groups": self.instance_security_groups
                    }
                }
            }
        }, indent=4)
        return plan_data
