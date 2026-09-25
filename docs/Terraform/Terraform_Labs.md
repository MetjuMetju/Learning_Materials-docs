### TERRAFORM SIMPLE LABS

### LAB 01 BASIC S3 BUCKET
```code
vi main.tf

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "lab" {
  bucket_prefix = "terraform-lab-"
}

output "bucket_name" {
  value = aws_s3_bucket.lab.bucket
}


# Commands:
terraform init
terraform plan
terraform apply
terraform output
terraform destroy


### LAB 02 VARIABLES

vi main.tf

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "lab" {
  bucket_prefix = var.bucket_prefix
}

output "bucket_name" {
  value = aws_s3_bucket.lab.bucket
}


vi variables.tf

variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "bucket_prefix" {
  type    = string
  default = "terraform-lab-02-"
}


# Commands
terraform init
terraform plan
terraform apply
terraform output
terraform destroy


### LAB 03 DATA SOURCE

vi main.tf

provider "aws" {
  region = "eu-central-1"
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

output "region" {
  value = data.aws_region.current.name
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}


# Commands:
terraform init
terraform plan
terraform apply
terraform output


### LAB 04 BASIC VPC

vi main.tf

provider "aws" {
  region = "eu-central-1"
}

resource "aws_vpc" "lab" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "terraform-lab-vpc"
  }
}

resource "aws_subnet" "lab" {
  vpc_id     = aws_vpc.lab.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "terraform-lab-subnet"
  }
}

output "vpc_id" {
  value = aws_vpc.lab.id
}

output "subnet_id" {
  value = aws_subnet.lab.id
}


# Commands:
terraform init
terraform plan
terraform apply
terraform output
terraform destroy


### LAB 05 EC2

vi main.tf

provider "aws" {
  region = var.aws_region
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }
}

resource "aws_instance" "lab" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  tags = {
    Name = "terraform-lab-ec2"
  }
}

output "instance_id" {
  value = aws_instance.lab.id
}


vi variables.tf

variable "aws_region" {
  type    = string
  default = "eu-central-1"
}
variable "instance_type" {
  type    = string
  default = "t3.micro"
}


# Commands:
terraform init
terraform plan
terraform apply
terraform output
terraform destroy


### LAB 06 MODULE

vi main.tf

provider "aws" {
  region = "eu-central-1"
}
module "bucket" {
  source = "./modules/bucket"
}
output "bucket_name" {
  value = module.bucket.bucket_name
}


vi modules/bucket/main.tf

resource "aws_s3_bucket" "this" {
  bucket_prefix = "terraform-module-"
}
output "bucket_name" {
  value = aws_s3_bucket.this.bucket
}


# Commands:

terraform init
terraform plan
terraform apply
terraform output
terraform destroy
```

### BASIC WORKFLOW

	- terraform init
	- terraform fmt
	- terraform validate
	- terraform plan
	- terraform apply
	- terraform destroy