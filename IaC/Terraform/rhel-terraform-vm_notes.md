```bash
### 1. PROJECT STRUCTURE

rhel-terraform/

rhel-terraform/
├── provider.tf
├── main.tf
├── variables.tf
├── outputs.tf
├── cloud-init/
│   └── user-data.yaml
└── images/
    └── rhel-base.qcow2   (OPTIONAL LOCAL IMAGE CACHE)

### 2. RHEL IMAGE SOURCE (IMPORTANT MISSING PART)

You MUST provide a base RHEL image:

OPTION A (manual download from Red Hat)
- RHEL 9 QCOW2 image from:
  https://access.redhat.com/downloads/content/rhel

OR

OPTION B (local prebuilt image path)
/var/lib/libvirt/images/rhel-9-base.qcow2
### 3. VARIABLES (ADD RHEL VERSION CONTROL)

rhel-terraform/variables.tf

variable "rhel_version" {
  default = "9.4"
}

variable "base_image" {
  default = "/var/lib/libvirt/images/rhel-9-base.qcow2"
}
### 4. PROVIDER

rhel-terraform/provider.tf

terraform {
  required_providers {
    libvirt = {
      source  = "dmacvicar/libvirt"
      version = "~> 0.7"
    }
  }
}

provider "libvirt" {
  uri = "qemu:///system"
}
### 5. VM DISK (THIS IS WHERE RHEL IMAGE IS USED)

rhel-terraform/main.tf

resource "libvirt_volume" "rhel_disk" {
  name   = "rhel-node1.qcow2"
  pool   = "default"

  # THIS IS THE ACTUAL RHEL IMAGE SOURCE
  source = var.base_image

  format = "qcow2"
}
### 6. CLOUD-INIT (OS POST-INSTALL CONFIG)

rhel-terraform/cloud-init/user-data.yaml

#cloud-config

hostname: rhel-node1

packages:
  - vim
  - curl
  - wget
  - git
  - net-tools

runcmd:
  - systemctl enable --now sshd
  - systemctl enable --now chronyd
  - systemctl enable --now firewalld
  - firewall-cmd --permanent --add-service=ssh
  - firewall-cmd --reload
### 7. DEPLOYMENT FLOW

terraform init
terraform plan
terraform apply -auto-approve
```
