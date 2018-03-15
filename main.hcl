provider "openstack" {
}

## node: orbit
resource "openstack_compute_instance_v2" "orbit" {
  name = "orbit"
  image_id = "f67e34fb-108d-4418-9a49-4a2dbde5a8f1"
  flavor_id = "44"
  key_pair = "id_rsa"
  security_groups = ["default"]

  network {
    name = "red de sergio.ferrete"
  }
}

# get float ip from pool
resource "openstack_networking_floatingip_v2" "getfip_1" {
  pool = "ext-net"
}

# associate existing float IP
resource "openstack_compute_floatingip_associate_v2" "fip_1" {
  # floating_ip = "172.22.201.108"
  # associate new float ip requested to the pool
  floating_ip = "${openstack_networking_floatingip_v2.getfip_1.address}"
  instance_id = "${openstack_compute_instance_v2.orbit.id}"
}

# create new volume, not attached
resource "openstack_blockstorage_volume_v2" "terraform" {
  name        = "openstack"
  description = "Volume create by terraform"
  size        = 5
}

# attach volume to orbit
resource "openstack_compute_volume_attach_v2" "attachedtorobit" {
  instance_id = "${openstack_compute_instance_v2.orbit.id}"
  volume_id = "${openstack_blockstorage_volume_v2.terraform.id}"
}
