import json

resource_type="openstack_compute_instance_v2"
resource_name="orbit"
instance_name="orbit"
instance_image_id="f67e34fb-108d-4418-9a49-4a2dbde5a8f1"
instance_flavor_id="44"
instance_key_pair="id_rsa"
instance_security_groups=["default"]

print(json.dumps(
{
    "resource": {
        resource_type: {
            resource_name: {
                "name": instance_name,
                "image_id": instance_image_id,
                "flavor_id": instance_flavor_id,
                "key_pair": instance_key_pair,
                "security_groups": instance_security_groups
            }
        }
    }
}, indent=4))
