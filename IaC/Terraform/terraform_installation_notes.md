# Terraform notes

## Installation official URL(s)
```code
https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
https://developer.hashicorp.com/terraform/language/v1-compatibility-promises
```

### Installation steps (Ubuntu)
```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update | grep hashicorp
cat /etc/apt/sources.list.d/hashicorp.list

sudo apt update
sudo apt-get install terraform
terraform -install-autocomplete
grep terraform ~/.bashrc
```

### CMDs:
```bash
terraform -v
terraform -help
terraform plan -help

### simple create file example:
mkdir terraform-demo
cd terraform-demo
------
vi main.tf
---
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}
provider "local" {}
resource "local_file" "hello" {
  content  = "Hello from Terraform"
  filename = "${path.module}/hello.txt"
}
---
------
terraform init
terraform plan
terraform apply # type yes
```
