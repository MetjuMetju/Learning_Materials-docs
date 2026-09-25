# TERRAFORM GUIDE CORE AREAS

### TERRAFORM BASICS

	- Infrastructure as Code tool for defining and managing infrastructure
	- IaC = Infrastructure as Code
	- Terraform configuration is written mainly in HCL
	- HCL = HashiCorp Configuration Language
	- Terraform uses configuration files to describe desired infrastructure
	- Terraform creates and manages resources through providers


### CORE TERRAFORM CONCEPTS

	- Provider
	- Resource
	- Data Source
	- Variable
	- Local Value
	- Output
	- Module
	- State
	- Backend
	- Dependency
	- Provisioner


### PROVIDERS

	- Connect Terraform to cloud platforms, services, and APIs
	- Provider = Plugin that allows Terraform to communicate with an API
	- AWS Provider
	- Azure Provider
	- Google Cloud Provider
	- Kubernetes Provider
	- GitHub Provider

##### Example:
```code
provider "aws" {
	region = "eu-central-1"
	}
```

### RESOURCES

	- Define infrastructure that Terraform should create and manage
	- Resource = Infrastructure object managed by Terraform
	- aws_instance
	- aws_s3_bucket
	- aws_vpc
	- aws_subnet
	- aws_security_group

##### Example
```code
resource "aws_s3_bucket" "example" {
	bucket = "my-example-bucket"
	}
```

### DATA SOURCES

	- Read existing information without creating the resource
	- Data Source = Existing information retrieved from a provider
	- Find existing VPC
	- Find existing AMI
	- Find existing AWS account information
	- Find existing Availability Zones

##### Example
```code
data "aws_availability_zones" "available" {
	state = "available"
	}
```

### VARIABLES

	- Allow configuration values to be supplied from outside the resource definitions
	- Input Variable = User supplied configuration value
	- string
	- number
	- bool
	- list
	- set
	- map
	- object

##### Example
```code
variable "region" {
	type    = string
	default = "eu-central-1"
}
```

### LOCAL VALUES

	- Define reusable values inside a Terraform configuration
	- Local Value = Named expression calculated inside Terraform
	- Useful for reducing repetition
	- Useful for naming conventions
	- Useful for calculated values

##### Example
```code
locals {
	environment = "production"
}
```

### OUTPUTS

	- Expose useful values after Terraform creates infrastructure
	- Output = Value displayed or passed to other Terraform configurations
	- Instance IP address
	- Load Balancer DNS name
	- VPC ID
	- S3 bucket name

##### Example
```code
output "bucket_name" {
	value = aws_s3_bucket.example.bucket
}
```

### MODULES

	- Package reusable Terraform configurations
	- Module = Collection of Terraform configuration files
	- Root Module = Main Terraform configuration
	- Child Module = Module called by another module
	- Public Modules = Modules available through the Terraform Registry
	- Private Modules = Modules stored in private registries

##### Example
```code
module "network" {
	source = "./modules/network"
}
```

### STATE

	- Terraform state records what infrastructure Terraform manages
	- State = Mapping between Terraform configuration and real infrastructure
	- terraform.tfstate
	- Terraform uses state to determine what needs to change
	- State should normally be stored securely
	- State can contain sensitive information


### BACKENDS

	- Define where Terraform state is stored
	- Backend = Storage location and mechanism for Terraform state
	- Local Backend
	- S3 Backend
	- Terraform Cloud
	- HCP Terraform

	- Remote state enables team collaboration
	- State locking helps prevent simultaneous conflicting changes


### TERRAFORM REGISTRY

	- Repository for Terraform providers and modules
	- Terraform Registry
	- Provider Registry
	- Module Registry
	- Public providers
	- Public modules


### TERRAFORM WORKFLOW

	- terraform init
	- Initialize working directory
	- Download providers and modules
	- Configure backend

	- terraform fmt
	- Format Terraform configuration

	- terraform validate
	- Check configuration syntax and consistency

	- terraform plan
	- Preview infrastructure changes

	- terraform apply
	- Create or update infrastructure

	- terraform destroy
	- Remove infrastructure managed by Terraform


### TERRAFORM CLI

	- CLI = Command Line Interface

	- terraform init
	- terraform fmt
	- terraform validate
	- terraform plan
	- terraform apply
	- terraform destroy
	- terraform show
	- terraform output
	- terraform state
	- terraform import
	- terraform workspace


### CONFIGURATION FILES

	- .tf
	- Main Terraform configuration file

	- .tfvars
	- Variable values file

	- terraform.tfvars
	- Automatically loaded variable values file

	- .terraform.lock.hcl
	- Records selected provider versions

	- terraform.tfstate
	- Terraform state file


### HCL BASICS

	- HCL = HashiCorp Configuration Language
	- Block
	- Argument
	- Expression
	- Attribute
	- String
	- Number
	- Boolean
	- List
	- Map
	- Object

##### Example
```code
resource "aws_instance" "web" {
	ami = "ami-example"
	instance_type = "t3.micro"
}
```

### DEPENDENCIES

	- Terraform determines dependencies between resources
	- Implicit Dependency = Dependency created by referencing another resource
	- Explicit Dependency = Dependency defined with depends_on
	- Terraform creates resources in dependency order

##### Example
```code
subnet_id = aws_subnet.main.id
```

### LIFECYCLE

	- Control how Terraform creates, updates, and destroys resources
	- create_before_destroy
	- prevent_destroy
	- ignore_changes
	- replace_triggered_by


### RESOURCE META ARGUMENTS

	- Meta Arguments = Special arguments supported by Terraform resources
	- count
	- for_each
	- depends_on
	- provider
	- lifecycle


### WORKSPACES

	- Manage separate Terraform state instances using the same configuration
	- Workspace = Separate state environment
	- Default Workspace
	- Development Workspace
	- Production Workspace

	- Common commands
	- terraform workspace list
	- terraform workspace new development
	- terraform workspace select development


### IMPORTING EXISTING INFRASTRUCTURE

	- Import infrastructure that already exists into Terraform management
	- terraform import
	- Import connects an existing resource to Terraform state
	- Configuration still needs to describe the imported resource


### SECRETS AND SENSITIVE DATA

	- Avoid hardcoding passwords, API keys, and credentials
	- Sensitive Variable = Variable whose value should be treated as sensitive
	- Environment Variables
	- Secret Managers
	- AWS Secrets Manager
	- HCP Vault
	- Terraform sensitive = true
	- Never commit secrets or state files containing sensitive information to Git


### TEAM COLLABORATION

	- Use remote state
	- Enable state locking where supported
	- Store Terraform configuration in Git
	- Review terraform plan before apply
	- Use consistent provider versions
	- Use reusable modules
	- Separate development and production environments


### TERRAFORM WITH AWS

	- Terraform
	- AWS Provider
	- AWS Infrastructure

	- Common AWS resources managed by Terraform

	- VPC = Virtual Private Cloud
	- Subnets
	- Route Tables
	- Internet Gateway
	- NAT Gateway = Network Address Translation Gateway
	- Security Groups
	- EC2 = Elastic Compute Cloud
	- S3 = Simple Storage Service
	- RDS = Relational Database Service
	- IAM = Identity and Access Management
	- Lambda
	- ELB = Elastic Load Balancing
	- ECS = Elastic Container Service
	- EKS = Elastic Kubernetes Service


### BASIC TERRAFORM ARCHITECTURE

	- Terraform Configuration
	- Provider
	- Resources
	- Data Sources
	- Variables
	- Modules
	- Outputs
	- State
	- Backend

	- Terraform reads configuration
	- Terraform loads providers
	- Terraform reads current state
	- Terraform compares desired state with real infrastructure
	- terraform plan shows changes
	- terraform apply makes changes
	- Terraform updates state


### BASIC TERRAFORM WORKFLOW

	- Write Terraform configuration
	- terraform init - Terraform initialization stage
	- terraform fmt
	- terraform validate
	- terraform plan
	- Review changes
	- terraform apply
	- Infrastructure is created or updated
	- Terraform state is updated

##### EXAMPLE:
```code
cat main.tf:
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

# Command (Backend default local initialization, set up modules):
terraform init

# "Get this Terraform project ready to work"

# will create folder (local working directory):
.terraform
# and file (dependency lock file):
.terraform.lock.hcl

# this line:
value = aws_s3_bucket.lab.bucket
# will download: AWS provider plugin (889 MB)
terraform-provider-aws_v6.62.0_x5

# Command:
terraform plan

# This command needs AWS credentials first to be configured:
aws --version
aws configure
AWS Access Key ID:     <your access key>
AWS Secret Access Key: <your secret key>
Default region name:  eu-central-1
Default output format: json
# Then:
ls -la ~/.aws/
ls -l ~/.aws/credentials
cat ~/.aws/config
aws sts get-caller-identity
# STS = AWS Security Token Service

# Aftur running plan command - the backend is where Terraform stores its state (terraform.tfstate).

mkdir -p terraform-learning/01-docker-nginx
cd terraform-learning/01-docker-nginx

vi main.tf
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
    }
  }
}
provider "docker" {						# Use Docker as configured by the Docker provider
}
resource "docker_image" "nginx" {		# Terraform should manage a Docker container.
										# resource type: docker_image
										# Terraform name: nginx

  name = "nginx:latest"
}
resource "docker_container" "nginx" {
  name  = "terraform-nginx"
  image = docker_image.nginx.image_id	# Docker provider
  ports {
    internal = 80
    external = 8080
  }
}

# Next commands:
terraform apply
docker ps
docker logs terraform-nginx

curl http://localhost:8080


```

- Created a Terraform configuration
- Added the Docker provider
- Used kreuzwerker docker provider
- Defined an Nginx Docker image
- Defined an Nginx Docker container
- Connected the container to the Nginx image
- Mapped container port 80 to host port 8080
- Ran terraform init
- Terraform downloaded the Docker provider
- Terraform created .terraform.lock.hcl

### TERRAFORM COMMANDS

### CHECK

- terraform --version
- terraform validate
- terraform fmt


### INIT

- terraform init


### PLAN

- terraform plan


### APPLY

- terraform apply


### STATE

- terraform state list
- terraform show
- terraform refresh


### DESTROY

- terraform destroy


### COMMON FLOW

- terraform init
- terraform fmt
- terraform validate
- terraform plan
- terraform apply
- terraform state list
- terraform destroy

### TERRAFORM LEARNING PRIORITY

	- 1. Terraform
	- 2. IaC = Infrastructure as Code
	- 3. HCL = HashiCorp Configuration Language
	- 4. Provider
	- 5. Resource
	- 6. Data Source
	- 7. Variable
	- 8. Output
	- 9. Module
	- 10. State
	- 11. Backend
	- 12. Dependency
	- 13. terraform init
	- 14. terraform plan
	- 15. terraform apply
	- 16. terraform destroy
	- 17. terraform fmt
	- 18. terraform validate
	- 19. count
	- 20. for_each
	- 21. depends_on
	- 22. lifecycle
	- 23. terraform import
	- 24. Remote State
	- 25. Terraform Registry


### TERRAFORM VS ANSIBLE

	- Terraform builds the infrastructure
	- Ansible configures the infrastructure

### TERRAFORM

	- Infrastructure as Code
	- Defines desired infrastructure state
	- Creates Docker image and container
	- Manages infrastructure lifecycle
	- Uses terraform plan
	- Uses terraform apply
	- Uses terraform destroy
	- Tracks resources in Terraform state

### ANSIBLE

	- Configuration management
	- Configures existing infrastructure
	- Can install and configure Docker
	- Can create and manage containers
	- Uses playbooks
	- Uses tasks and modules
	- Runs with ansible-playbook
	- Does not use Terraform state


### SIMPLE DIFFERENCE

- Terraform
	- Create and manage infrastructure
- Ansible
	- Configure and manage systems


### EXAMPLE

Terraform

- Create Docker container
- Define ports
- Manage container lifecycle

Ansible

- Install Docker
- Configure Docker
- Start container
- Configure application
