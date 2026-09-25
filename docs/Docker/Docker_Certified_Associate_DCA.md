### Docker Certified Associate (DCA)

1. Orchestration 25%
2. Image Creation, Management, and Registry 20%
3. Installation and Configuration 15%
4. Networking 15%
5. Security 15%
6. Storage and Volumes 10%


Content Limits
Domain 1: Orchestration (25% of exam)
Content may include the following:
● Complete the setup of a swarm mode cluster, with managers and worker nodes
● Describe and demonstrate how to extend the instructions to run individual containers into
running services under swarm.
● Describe the importance of quorum in a swarm cluster.
● Describe the difference between running a container and running a service.
● Interpret the output of “docker inspect” commands.
● Convert an application deployment into a stack file using a YAML compose file with "docker
stack deploy"
● Manipulate a running stack of services.
● Describe and demonstrate orchestration activities.
● Increase the number of replicas.
● Add networks, publish ports.
● Mount volumes.
● Describe and demonstrate how to run replicated and global services.
● Apply node labels to demonstrate placement of tasks.
Describe and demonstrate how to use templates with “docker service create”.
● Identify the steps needed to troubleshoot a service not deploying.
● Describe how a Dockerized application communicates with legacy systems.
● Describe how to deploy containerized workloads as Kubernetes pods and deployments.
● Describe how to provide configuration to Kubernetes pods using configMaps and secrets.
Domain 2: Image Creation, Management, and Registry (20% of exam)
Content may include the following:
● Describe the use of Dockerfile.
● Describe options, such as add, copy, volumes, expose, entry point.
● Identify and display the main parts of a Dockerfile.
● Describe and demonstrate how to create an efficient image via a Dockerfile.
● Describe and demonstrate how to use CLI commands to manage images, such as list,
delete, prune, rmi.
Describe and demonstrate how to inspect images and report specific attributes using filter
and format
● Describe and demonstrate how to tag an image.
● Describe and demonstrate how to apply a file to create a Docker image.
● Describe and demonstrate how to display layers of a Docker image
● Describe and demonstrate how to modify an image to a single layer.
● Describe and demonstrate registry functions.
● Deploy a registry.
● Log into a registry.
● Utilize search in a registry.
● Push an image to a registry.
● Sign an image in a registry.
● Pull and delete images from a registry.
Domain 3: Installation and Configuration (15% of exam)
Content may include the following:
● Describe sizing requirements for installation.
● Describe and demonstrate the setup of repo, selection of a storage driver, and installation
of the Docker engine on multiple platforms.
● Describe and demonstrate configuration of logging drivers (splunk, journald, etc.).
● Describe and demonstrate how to set up swarm, configure managers, add nodes, and
setup the backup schedule.
Describe and demonstrate how to create and manage user and teams.
● Describe and demonstrate how to configure the Docker daemon to start on boot.
● Describe and demonstrate how to use certificate-based client-server authentication to
ensure a Docker daemon has the rights to access images on a registry.
● Describe the use of namespaces, cgroups, and certificate configuration.
● Describe and interpret errors to troubleshoot installation issues without assistance.
● Describe and demonstrate the steps to deploy the Docker engine, UCP, and DTR on AWS
and on-premises in an HA configuration.
● Describe and demonstrate how to configure backups for UCP and DTR.
Domain 4: Networking (15% of exam)
Content may include the following:
● Describe the Container Network Model and how it interfaces with the Docker engine and
network and IPAM drivers.
● Describe the different types and use cases for the built-in network drivers.
● Describe the types of traffic that flow between the Docker engine, registry and UCP
controllers.
● Describe and demonstrate how to create a Docker bridge network for developers to use for
their containers.
● Describe and demonstrate how to publish a port so that an application is accessible
externally.
● Identify which IP and port a container is externally accessible on.
● Compare and contrast “host” and “ingress” publishing modes.
● Describe and demonstrate how to configure Docker to use external DNS.
● Describe and demonstrate how to use Docker to load balance HTTP/HTTPs traffic to an
application (Configure L7 load balancing with Docker EE).
● Understand and describe the types of traffic that flow between the Docker engine, registry,
and UCP controllers
Describe and demonstrate how to deploy a service on a Docker overlay network.
● Describe and demonstrate how to troubleshoot container and engine logs to resolve
connectivity issues between containers.
● Describe how to route traffic to Kubernetes pods using ClusterIP and NodePort services.
● Describe the Kubertnetes’ container network model.
Domain 5: Security (15% of exam)
Content may include the following:
● Describe security administration and tasks.
● Describe the process of signing an image.
● Describe default engine security.
● Describe swarm default security.
● Describe MTLS.
● Describe identity roles.
● Compare and contrast UCP workers and managers.
● Describe the process to use external certificates with UCP and DTR.
● Describe and demonstrate that an image passes a security scan.
Describe and demonstrate how to enable Docker Content Trust.
● Describe and demonstrate how to configure RBAC with UCP.
● Describe and demonstrate how to integrate UCP with LDAP/AD.
● Describe and demonstrate how to create UCP client bundles.
Domain 6: Storage and Volumes (10% of exam)
Content may include the following:
● Identify the correct graph drivers to uses with various operating systems.
● Describe and demonstrate how to configure devicemapper.
● Compare and contrast object and block storage and when they should be used.
● Describe how an application is composed of layers and where these layers reside on the
filesystem.
● Describe the use of volumes are used with Docker for persistent storage.
● Identify the steps to take to clean up unused images on a filesystem and DTR.
● Describe and demonstrate how storage can be used across cluster nodes.
● Describe how to provision persistent storage to a Kubernetes pod using persistentVolumes.
● Describe the relationship between container storage interface drivers, storageClass,
persistentVolumeClaim and volume objects in Kubernetes


1. Orchestration — 25%
   1.1 Swarm cluster
   1.2 Containers vs services
   1.3 Service management
   1.4 Scheduling and placement
   1.5 Stacks
   1.6 Troubleshooting
   1.7 Legacy integration
   1.8 Kubernetes basics

2. Image Creation, Management, and Registry — 20%
   2.1 Dockerfile
   2.2 Image creation
   2.3 Layers and cache
   2.4 Image management
   2.5 Image modification
   2.6 Registry
   2.7 Image signing

3. Installation and Configuration — 15%
   3.1 Docker Engine installation
   3.2 Docker daemon
   3.3 Logging
   3.4 Swarm setup
   3.5 Users and teams
   3.6 Certificates
   3.7 Linux fundamentals
   3.8 Troubleshooting
   3.9 Docker Enterprise

4. Networking — 15%
   4.1 Container Network Model
   4.2 Network drivers
   4.3 Bridge networking
   4.4 Port publishing
   4.5 Publishing modes
   4.6 DNS
   4.7 Load balancing
   4.8 Overlay networking
   4.9 Networking troubleshooting
   4.10 Kubernetes networking

5. Security — 15%
   5.1 Docker security
   5.2 Swarm security
   5.3 Image security
   5.4 Certificates
   5.5 Identity and access
   5.6 Authentication
   5.7 Client access

6. Storage and Volumes — 10%
   6.1 Image storage
   6.2 Storage drivers
   6.3 Storage types
   6.4 Docker volumes
   6.5 Storage cleanup
   6.6 Cluster storage
   6.7 Kubernetes persistent storage
   6.8 Kubernetes CSI

1. ORCHESTRATION — 25%
   1.1 Swarm cluster
       managers
       workers
       swarm init
       swarm join
       quorum

   1.2 Containers vs services
       docker run
       docker service create
       service lifecycle
       replicated services
       global services

   1.3 Service management
       docker service ls
       docker service ps
       docker service inspect
       docker service update
       scaling replicas
       publish ports
       attach networks
       mount volumes

   1.4 Scheduling and placement
       node labels
       placement constraints
       service templates

   1.5 Stacks
       Compose YAML
       docker stack deploy
       docker stack services
       docker stack ps
       updating stacks

   1.6 Troubleshooting
       service not deploying
       task failures
       node problems
       docker inspect

   1.7 Legacy integration
       Dockerized applications
       communication with legacy systems

   1.8 Kubernetes basics
       Pods
       Deployments
       ConfigMaps
       Secrets


2. IMAGE CREATION, MANAGEMENT, REGISTRY — 20%
   2.1 Dockerfile
       FROM
       RUN
       COPY
       ADD
       ENV
       ARG
       EXPOSE
       VOLUME
       CMD
       ENTRYPOINT

   2.2 Image creation
       docker build
       build context
       efficient Dockerfiles
       .dockerignore

   2.3 Layers and cache
       image layers
       build cache
       layer inspection
       minimizing layers

   2.4 Image management
       docker images
       docker image ls
       docker image inspect
       docker image rm
       docker rmi
       docker image prune
       filter
       format
       tagging

   2.5 Image modification
       docker commit
       creating images from containers
       single-layer images

   2.6 Registry
       registry deployment
       docker login
       search
       push
       pull
       delete

   2.7 Image signing
       signing images
       trusted images
       Content Trust

3. INSTALLATION AND CONFIGURATION — 15%
   3.1 Docker Engine installation
       installation requirements
       repositories
       Linux
       other platforms
       storage driver selection

   3.2 Docker daemon
       daemon configuration
       daemon.json
       start on boot
       daemon troubleshooting

   3.3 Logging
       logging drivers
       json-file
       journald
       splunk

   3.4 Swarm setup
       managers
       workers
       node configuration
       backups

   3.5 Users and teams
       user management
       team management

   3.6 Certificates
       client-server TLS
       registry certificates
       certificate authentication

   3.7 Linux fundamentals
       namespaces
       cgroups
       certificates

   3.8 Troubleshooting
       installation errors
       daemon errors
       configuration errors

   3.9 Docker Enterprise
       UCP
       DTR
       HA
       AWS
       on-premises
       backups

4. NETWORKING — 15%
   4.1 Container Network Model
       CNM
       Docker Engine
       network drivers
       IPAM

   4.2 Network drivers
       bridge
       host
       overlay
       none
       macvlan

   4.3 Bridge networking
       create network
       connect containers
       container communication
       DNS

   4.4 Port publishing
       -p
       published port
       target container port
       external access

   4.5 Publishing modes
       host mode
       ingress mode

   4.6 DNS
       external DNS
       container DNS
       service discovery

   4.7 Load balancing
       HTTP/HTTPS
       L7 load balancing
       Docker EE

   4.8 Overlay networking
       Swarm overlay
       service communication
       multi-node networking

   4.9 Networking troubleshooting
       container connectivity
       engine logs
       container logs
       network inspection

   4.10 Kubernetes networking
       container network model
       ClusterIP
       NodePort
       Pod traffic

5. SECURITY — 15%
   5.1 Docker security
       default engine security
       namespaces
       cgroups
       capabilities

   5.2 Swarm security
       Swarm security
       manager/worker security
       MTLS

   5.3 Image security
       image signing
       security scanning
       Content Trust

   5.4 Certificates
       TLS
       MTLS
       external certificates
       UCP certificates
       DTR certificates

   5.5 Identity and access
       roles
       RBAC
       UCP workers
       UCP managers

   5.6 Authentication
       LDAP
       Active Directory

   5.7 Client access
       UCP client bundles

6. STORAGE AND VOLUMES — 10%
   6.1 Image storage
       image layers
       filesystem layers
       layer locations

   6.2 Storage drivers
       graph drivers
       driver selection
       devicemapper

   6.3 Storage types
       object storage
       block storage
       use cases

   6.4 Docker volumes
       docker volume create
       persistent data
       volume mounting
       volume management

   6.5 Storage cleanup
       unused images
       unused containers
       filesystem cleanup
       DTR cleanup

   6.6 Cluster storage
       storage across nodes
       shared storage

   6.7 Kubernetes persistent storage
       PersistentVolume
       PersistentVolumeClaim
       StorageClass

   6.8 Kubernetes CSI
       Container Storage Interface
       CSI drivers
       storage provisioning
       volume objects

### 1. Docker fundamentals
docker run
docker ps
docker exec
docker logs
docker inspect
docker stop
docker start
docker rm
docker image rm
docker top
docker login
docker images
docker pull
docker tag

Dockerfile instruction:
RUN
CMD
BUILD
START
ENTRYPOINT
ENV
ARG
EXPOSE

### 2. Images
Dockerfile
docker build
build context
layers
cache
BuildKit
Buildx
tags
registry
push/pull

### 3. Networking
bridge
host
overlay
ports
DNS
service discovery
ingress

### 4. Storage
volumes
bind mounts
storage drivers
persistent storage
Kubernetes PV/PVC

### 5. Swarm
docker swarm init
managers/workers
quorum
docker node
docker service
replicas
global services
placement
overlay networks
secrets/configs
docker stack
troubleshooting

### 6. Security
namespaces
cgroups
TLS/mTLS
image signing
Content Trust
RBAC
certificates
security scanning
Phase 7 — Enterprise DCA material
MKE/UCP
MSR/DTR
HA
backups
registry administration
LDAP/AD
client bundles

### 8. Kubernetes basics

Pods
Deployments
ConfigMaps
Secrets
ClusterIP
NodePort
PV
PVC
StorageClass
CSI

- Modern Kubernetes does not require Docker Engine as its container runtime.
- Kubernetes had built-in dockershim specifically to make Docker Engine work as its runtime.
- Kubernetes removed dockershim in Kubernetes 1.24
- Today Kubernetes requires a CRI-compatible runtime
- Common choices include containerd and CRI-O. Docker Engine itself doesn't implement CRI.
- Mirantis acquired Docker Enterprise in November 2019

NORMAL DOCKER                  KUBERNETES
docker build                   kubectl apply
docker run                     kubectl run
docker ps                      kubectl get pods
docker logs                    kubectl logs
docker exec                    kubectl exec
docker network                 kubectl get svc
docker volume                  kubectl get pv,pvc
docker swarm                   Kubernetes cluster


### Docker vs K8s:

Dockerfile                  - describes how to build an image.
docker build                - creates the image.
docker push                 - puts the image into a registry.
Kubernetes YAML             - describes how to deploy/run the image.
kubectl apply -f app.yaml   - sends that desired configuration to Kubernetes.

- Kubernetes itself does not build Docker/OCI images.
- Docker / BuildKit - builds the image.
- Registry - stores/distributes the image.
- Kubernetes - pulls the image and runs/manages containers from it.
- kubectl apply - tells Kubernetes what/how to run, not how to build the image.
- Kubernetes can be combined with separate image-building tools (Kaniko, BuildKit, Buildah, Tekton, CI/CD systems, etc.)


### Docker part:
1. FILES:
myapp/
Dockerfile
app.py

2. BUILD IMAGE
cd myapp
docker build -t myregistry/myapp:1.0 .

3. PUSH IMAGE
docker push myregistry/myapp:1.0

### k8s part:
1. FILES:
myapp.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry/myapp:1.0

2. RUN IT IN KUBERNETES
kubectl apply -f myapp.yaml

3. CHECK IT
kubectl get pods
kubectl logs <pod-name>


### SWARN
```code
docker node ls
docker service create --replicas 3 nginx
docker node promote NODE
docker service inspect SERVICE
docker service scale SERVICE=5
# purpose of a Swarm service: define and maintain a desired state for containers
# tasks belonging to a Swarm service:
docker service ps SERVICE

# Swarm service should run exactly one task on every eligible node. Which service mode should be used?
global
```

### Linux namespaces
### purpose of cgroups

docker push registry.example.com/myapp:1.0

### bind mount
- A mount that maps a host filesystem path into a container
### network drivers
- bridge (default one)
- host
docker network create mynet
docker network connect NETWORK CONTAINER
Docker's embedded DNS
...

### Docker Trusted Registry (DTR)
- DTR became Mirantis Secure Registry (MSR)