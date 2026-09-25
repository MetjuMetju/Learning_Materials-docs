### DOCKER BASIC GUIDE

### BASIC CONCEPT

- Docker is a containerization platform
- packages applications with dependencies
- runs applications in isolated containers
- creates containers from images
- manages container lifecycle
- provides networking
- provides persistent storage
- makes applications portable


01  Docker architecture
02  Images & Dockerfiles
03  Build / BuildKit / Buildx
04  Containers & lifecycle
05  Docker CLI
06  Networking
07  Volumes & storage
08  Docker Compose & stacks
09  Registries / Docker Hub / DTR / MSR
10  Security / certificates / RBAC
11  Resource limits / namespaces / cgroups
12  Logging / troubleshooting
13  Docker Swarm / Kubernetes / orchestration
14  Installation / configuration / UCP / HA / backup

### DOCKER ARCHITECTURE

Docker Client

- Docker CLI
- Docker Compose

Docker Host

- Docker Daemon
- Images
- Containers
- Networks
- Volumes

Docker Registry

- Docker Hub
- Private Registry


### IMAGE

- Read only template for containers
- Contains application and dependencies
- Built using Dockerfile
- Stored locally or in a registry


### CONTAINER

- Running instance of an image
- Isolated application environment
- Can be started and stopped
- Can expose ports
- Can use volumes


### DOCKERFILE

- FROM    Base image
- RUN     Execute commands
- COPY    Copy files
- WORKDIR Set working directory
- EXPOSE  Document port
- CMD     Default command


### BASIC FLOW

- Dockerfile
- Image
- Container
- Application


### DOCKER COMMANDS

### CHECK

    docker --version
    docker info
    docker ps
    docker ps -a
    docker images


### IMAGE

    docker pull nginx:latest
    docker images
    docker rmi nginx:latest


### CONTAINER

    docker run -d --name terraform-nginx -p 8080:80 nginx:latest
    docker ps
    docker stop terraform-nginx
    docker start terraform-nginx
    docker restart terraform-nginx
    docker rm terraform-nginx


### CHECK CONTAINER

    docker logs terraform-nginx
    docker port terraform-nginx
    docker inspect terraform-nginx
    docker exec -it terraform-nginx bash


### TEST

    curl http://localhost:8080




06. Docker networking, the main choices are:

- bridge - containers on one Docker host, normal standalone Docker networking
- host - container uses the host's network stack, no separate container network isolation
- overlay - containers/services across Docker hosts - mainly Swarm
- none - no normal container networking
- macvlan - container gets its own MAC/network identity - useful for particular network-integration cases

- CONTAINER - CONTAINER on same host - bridge
- CONTAINER/SERVICE - CONTAINER/SERVICE across Swarm nodes - overlay
- DTR components across DTR nodes - dtr-ol

```code
# Commands:
docker network create --driver overlay my-overlay
# Creates:
Name:   my-overlay
Driver: overlay

docker network ls
NETWORK ID     NAME        DRIVER
abc123         bridge      bridge
def456         my-overlay  overlay
ghi789         dtr-ol      overlay

# DTR creates its own network:
Name:   dtr-ol
Driver: overlay

# Normal Docker network:
docker network ls
docker network inspect bridge
# Swarm overlay:
docker network ls
docker network inspect my-overlay

# DTR:
docker network ls
docker network inspect dtr-ol

# Check Driver:
- bridge - Driver: bridge
- my-overlay - Driver: overlay
- dtr-ol - Driver: overlay

09.  DTR / MSR

stores Docker images
distributes images
controls access
scans images
supports image signing

Networks
dtr-ol
type: overlay
allows DTR/MSR components on different nodes
to communicate and replicate data

Basic workflow
docker login REGISTRY
docker tag myapp:1.0 REGISTRY/myapp:1.0
docker push REGISTRY/myapp:1.0
docker pull REGISTRY/myapp:1.0

Know
repositories
images
tags
registry authentication
image scanning
image signing
replication
garbage collection
dtr-ol
DTR/MSR troubleshooting

DCA focus
deploy registry
log into registry
search registry
push images
pull images
delete images
sign images
understand dtr-ol


### Basic open-source Docker local registry example:
docker run -d -p 5000:5000 --name registry registry:3
docker tag nginx:latest localhost:5000/nginx:latest
docker push localhost:5000/nginx:latest

IMAGE REGISTRY OPTIONS

Docker Hub
    hosted by Docker
    easiest general-purpose choice
    public + private images
    good for small projects
    security: Docker Scout / scanning
    pay for higher limits/features

GitLab Container Registry
    hosted by GitLab or self-hosted GitLab
    best when using GitLab
    repository + CI/CD + registry together
    security scanning integrated
    pay depending on GitLab plan/usage

GitHub Container Registry
    hosted by GitHub
    best when using GitHub
    GitHub repository + Actions + registry
    integrates with GitHub permissions
    pay depending on storage/transfer/plan

Amazon ECR
    hosted by AWS
    best when infrastructure is AWS
    integrates with IAM + ECS + EKS
    vulnerability scanning
    pay for storage/transfer/scanning

Azure Container Registry
    hosted by Microsoft Azure
    best when infrastructure is Azure
    integrates with Azure + AKS
    security/scanning features
    Basic / Standard / Premium tiers

Google Artifact Registry
    hosted by Google Cloud
    best when infrastructure is Google Cloud
    integrates with GKE + Google Cloud IAM
    vulnerability scanning available
    pay for storage/transfer

Harbor
    you operate it yourself
    independent of GitHub/GitLab/AWS/Azure
    private enterprise registry
    vulnerability scanning with Trivy
    access control
    replication
    policies
    more administration work

Docker Registry
    you operate it yourself
    basic registry
    simple image storage/distribution
    fewer enterprise features
    useful for simple/private deployments

DTR / MSR
    enterprise registry
    DTR = Docker Trusted Registry
    MSR = Mirantis Secure Registry
    Docker Enterprise / Mirantis ecosystem
    enterprise access/security/replication
    relevant to DCA material
```


### ADD vs COPY in Dockerfile

### COPY

- Copies files and directories from the build context into the image.

### Example:

    COPY app.conf /etc/app.conf

Use COPY by default.


### ADD

- Does everything COPY does, plus:

    - 1. Can extract local tar archives automatically.
    - 2. Can fetch URLs in some Docker builders.

### Example:

    ADD app.tar.gz /app/

The tar archive can be automatically extracted.

- COPY = simple file copy
- ADD = copy plus extra features
- Prefer COPY unless you specifically need an ADD feature such as automatic tar extraction.


### DOCKER COMPOSE container_name

- If you DO NOT specify:

        container_name:

- Docker Compose automatically generates a container name.

- The traditional pattern is:
        
        <project-name>-<service-name>-<number>


- For example:

        istrosec-dev-app01-istrosec-1


- where:

        istrosec-dev-app01
            = Compose project name

        istrosec
            = service name

        1
            = first container instance