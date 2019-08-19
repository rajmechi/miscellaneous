
# The Provider block sets up the vSphere provider - How to connect to vCenter. Note the use of
# variables to avoid hardcoding credentials here

provider "vsphere" {
  user           = "${var.vsphere_user}"
  password       = "${var.vsphere_password}"
  vsphere_server = "${var.vsphere_server}" 
  allow_unverified_ssl = true
}


# The Data sections are about determining where the virtual machine will be placed. 
# Here we are naming the vSphere DC, the cluster, datastore, virtual network and the template
# name. These are called upon later when provisioning the VM resource

data "vsphere_datacenter" "dc" {
  name = "DL-BDJSRL01-Lab"
}

data "vsphere_datastore" "datastore" {
  name          = "BDJSRL01-DL-Lab01-MU-GL-VX3C00-01"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_compute_cluster" "cluster" {
  name          = "${var.clustertouse}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "network" {
  name          = "${var.vmnetworktouse}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_virtual_machine" "template" {
  name          = "${var.templatetouse}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}


# you can output the data gathered above

output "datastore-address-is" {
  value = "${data.vsphere_datastore.datastore}"
}

output "cluster-is" {
  value = "${data.vsphere_compute_cluster.cluster}"
}

output "network-is" {
  value = "${data.vsphere_network.network}"
}

output "template-is" {
  value = "${data.vsphere_virtual_machine.template}"
}


# The Resource section creates the virtual machine, in this case
# from a template

resource "vsphere_virtual_machine" "vm" {
  
  name             = "dev1a10"
  resource_pool_id = "${data.vsphere_compute_cluster.cluster.resource_pool_id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"
  #folder = 
  num_cpus = 2
  memory   = 8192
  guest_id = "${data.vsphere_virtual_machine.template.guest_id}"
  #scsi_type = "${data.vsphere_virtual_machine.template.scsi_type}"
  wait_for_guest_net_timeout = 3 
 
  network_interface {
    network_id   = "${data.vsphere_network.network.id}"
    adapter_type = "${data.vsphere_virtual_machine.template.network_interface_types[0]}"
   }

  disk {
    label            = "disk0"
    size             = "${data.vsphere_virtual_machine.template.disks.0.size}"
    #eagerly_scrub    = "${data.vsphere_virtual_machine.template.disks.0.eagerly_scrub}"
    thin_provisioned = "${data.vsphere_virtual_machine.template.disks.0.thin_provisioned}"
  }

  disk {
    label       = "disk1"
    size        = "20"
    thin_provisioned = "true"
    #datastore_id     = "${data.vsphere_datastore.datastore.id}"
    unit_number = 1
  }
  
  disk {
    label       = "disk2"
    size        = "20"
    thin_provisioned = "true"
    #datastore_id     = "${data.vsphere_datastore.datastore.id}"
    unit_number = 2
  }

  clone {
    template_uuid = "${data.vsphere_virtual_machine.template.id}"

    customize {
      linux_options {
        host_name = "${var.servername}"
        domain    = "xxxx.com"
      }
      network_interface {
         ipv4_address = "10.10.10.11"
         ipv4_netmask = 24
         dns_server_list = ["10.11.11.11", "1.1.1.1"]
      }
      ipv4_gateway = "x.x.x.x"
      dns_suffix_list = ["xxxx.com", "xxx.xxx.com"] 
    }
  }
 
}

output "my_ip_address" {
  value = "${vsphere_virtual_machine.vm.default_ip_address}"
}


