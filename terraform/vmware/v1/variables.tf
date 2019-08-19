# provider vars

variable "vsphere_server" {
    description = "vsphere server for the environment - EXAMPLE: vcenter01.hosted.local"
    default = "xxxxxx"
}

variable "vsphere_user" {
    description = "vsphere server for the environment - EXAMPLE: vsphereuser"
    default = "xxxxxxx"
}

variable "vsphere_password" {
    description = "vsphere server password for the environment"
}

variable "servername" {
    description = "server name"
    default = "xxxxx"
}

#data vare

variable "clustertouse" {
    description = "cluster name to create vm"
    default = "xxxxxx"
}

variable "vmnetworktouse" { 
    description = "what network to use"
    default = "xxxxx"
}

variable "templatetouse" {
    description = "ehat template to use"
    default = "xxxx"
}
