# CKA Domains & Competencies Topics

https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/


##### 1. STORAGE - 10%
##### 2. TROUBLESHOOTING - 30%
##### 3. WORKLOADS & SCHEDULING - 15%
##### 4. CLUSTER ARCHITECTURE, INSTALLATION & CONFIGURATION - 25%
##### 5. SERVICES & NETWORKING - 20%


Core Concepts
    Cluster Architecture
    API Primitives
    Services & Other Network Primitives
Scheduling
    Labels & Selectors
    Daemon Sets
    Resource Limits
    Multiple Schedulers
    Manual Scheduling
    Scheduler EventsExamCert
    Configure Kubernetes Scheduler
Logging & Monitoring
    Monitor Cluster Components
    Monitor Cluster Components Logs
    Monitor Applications
    Application Logs
Application Lifecycle Management
    Rolling Updates and Rollbacks in Deployments
    Configuring Applications
    Scale Applications
    Self-Healing Applications
Cluster Maintenance
    Cluster Upgrade Process
    Operating System Upgrades
    Backup and Restore Methodologies
Security
    Authentication & Authorization
    Kubernetes Security
    Network Policies
    TLS Certificates for Cluster Components
    Image Security
    Network Polices
    Security Contexts
    Secure Persistent Key Value Store
Storage
    Persistent Volumes
    Access Modes for Volumes
    Persistent Volume Claims
    Kubernetes Storage Object
    Configure Applications with Persistent Storage
Networking
    Pre-Requisites - Network, Switching, Routing, Tools
    Pre-Requisites - Network Namespaces
    Pre-Requisites - Networking in Docker
    Networking Configuration on Cluster Nodes
    Service Networking
    POD Networking Concepts
    Network Loadbalancer
    Ingress
    Cluster DNSExamCert
    CNI
Installation, Configuration & Validation
    Design a Kubernetes Cluster
    Install Kubnernetes Master and Nodes
    Secure Cluster Communication
    HA Kubernetes Cluster
    Kubenetes Release Binaries
    Provision Infrastructure
    Choose a Network Solution
    Kubernetes Infrastructure Config
    Run & Analyze end-to-end test
    Node end-to-end tests
Troubleshooting
    Application Failure
    Control Plane Failure
    Worker Node Failure
    Networking

### Pod
- minimal component (element)
- running on one node
- has at least one container ("pause" container) or more containers (by usin also side-cars - e.g. for fluentd, filebeat)
- defining:
    - specification of container
    - livenes and readiness probes
    - resource limits (hard limits, min. limits, time of overlaps)
    - restart policies (always - restart when fail, on failure - if not 0 code, never = never restart
    - resart policy - container policy - if more pods in setup - on failure - restarting just this one pod which failed
    - security context (calls on kernel, allowed chown, set user ID)

- liveness probe restarts a broken container
- readiness probe stops sending traffic to a pod that is temporarily busy or not ready yet

### Pod - composite containers
- sidecar - e.g. filebeat for logs
- Ambasador - e.g. for network communiation or compute with cache
- Adapter - for transating data and modifing data to next pods
- init container - first starting container - when done - other pods can start

### Replica controller, ReplicaSet
- ReplicaSet - newer generation of replica controller with ability to work with selectors
- maintain a stable set of replica Pods running at any given time (not containers)
- implementing rolling updates
- If there are fewer pods than required (or if a pod crashes), it instantly creates new pods using its defined pod template
- Scaling Down: If there are too many pods, it deletes the extra ones to match the target number
- Label Selectors: It identifies which pods belong to it using a specific label selector

### Deployment
- configuring pods via ReplicaSet controller
- offers also declarative updates - desired states
- update of deployment creates new ReplicaSet - offers rollback to previous version

### Jobs, CronJobs
- creates Pods and checking succesfull result
- Kubernetes Jobs can run multiple Pods in parallel
- You can use a Job to run multiple Pods in parallel
- CronJob is a built-in workload resource used to automate and run short-lived, discrete tasks on a repeating schedule
- Job can recreate failed Pod or run new containers
- CronJob can recreate Job based on calendar

### DeamonSet
- similar to deployments
- startings Pods just on one node and always just one instance of the POD
- when added now node to cluster - pod is auto created there

### StatefulSet
- similar to deployments
- assigning titles/names for Pods and PersistentVolumes for stateful apps (e.g. DB)
- Provides stable identity for Pods:
    - Stable Pod names
    - Stable network identity
    - Ordered creation/deletion
    - Stable storage when PVCs are used

- StatefulSet is not storage. Storage is optional.
- for StatefulSet data to survive Pod recreation, persistent storage must be defined.

### Services

- Service provides:
    - Stable virtual IP + DNS name for accessing Pods
    - DNS name
    - Load balancing to Pods
    - Service Discovery - Finds a Service by DNS name or system variable of pod or DNS in cluster
    - mapping ports
    - using selectors

Example:
my-service.default.svc.cluster.local
Service ClusterIP
Pod
### Service Types:
- ClusterIP - exposed uniq IP
- NodePort - exposed port on node of Pod
- LoadBalancer - exposed service (port) on external LB, for IaaS (AWS, Azure...)
- ExternalName - exposed CNAME in cluster DNS

### Service Discovery
- Mechanism to find a Service by name.
- Usually automatic via DNS, not defined separately.
- Defined automatically by: Service + CoreDNS (kind: Service - DNS name created - Service Discovery)

### Ingress
- rules for reverse proxy
- rules for routing of HTTP(s)
- offers SSL offloading
- it is not external LB

### Volumes
- allows sharing files between Pods
- can use also NFS share and also configuration of cluster k8s cluster
- policy types: readonly many, read write one, read write many
- volume types:
    - emptyDir
    - hostPath
    - gcePersistentDisk
    - awsElasticBlockStore
    - nfs
    - glusterfs
    - cephfs
    - secret

### Persistent Volumes types:
- PersistentVolume
    - hostPath, NFS, iSCSI
    - independent on nodes
- PersistentVolumeClaim
    - request for persistent volume from Pod
    - covers amount, AccessMode, StorageClass
- StorageClass
    - can define QoS level
    - support dynamic (IaaS) created storage


### pull policy
imagePullPolicy: Never is not “restart only once.”
Kubernetes may start the container only if image already exists in the node's container runtime.
It will never pull the image from a registry.
imagePullPolicy: Never means:
Kubernetes will only start ai-backend:1.0 if that image exists in the containerd image store.

IfNotPresent will look in containerd, not Docker, and then try to pull ai-backend:1.0 from a registry.

### Commands:
kubectl get pods -A --no-headers | wc -l
kubectl get pods -A | grep -E 'Error|ContainerStatusUnknown|ErrImageNeverPull|CrashLoopBackOff' | head -50
kubectl get svc
kubectl get deploy -A
kubectl get rs -A --no-headers | grep -E 'py-container|jenkins|harbor-registry|harbor-core|rag'
##### what containerd is running
sudo ctr -n k8s.io tasks ls
sudo ctr -n k8s.io containers ls
sudo crictl ps -a
sudo crictl ps -a --state Exited -q | xargs -r sudo crictl rm
sudo crictl images | grep -E 'ai-backend|REPOSITORY'
sudo ctr -n k8s.io images ls | grep -i ai-backend


##### Remove all Failed/Succeeded pod objects
kubectl delete pods -A --field-selector=status.phase=Failed
kubectl delete pods -A --field-selector=status.phase=Succeeded
kubectl get pods -A --no-headers | wc -l
##### Remove the ContainerStatusUnknown garbage
kubectl get pods -A --no-headers | \
awk '$4=="ContainerStatusUnknown" {print $1, $2}' | \
while read ns pod; do
    kubectl delete pod -n "$ns" "$pod" \
      --force --grace-period=0 \
      --ignore-not-found
done
##### Clean old zero-replica ReplicaSets
kubectl get rs -A --no-headers | \
awk '$3==0 && $4==0 {print $1, $2}' | \
while read ns rs; do
    echo "Deleting old ReplicaSet: $ns/$rs"
    kubectl delete rs -n "$ns" "$rs" --ignore-not-found
done
##### clean old Jobs
kubectl get jobs -A --no-headers | \
awk '$3=="0" && $4=="1" {print $1, $2}' | \
while read ns job; do
    kubectl delete job -n "$ns" "$job" --ignore-not-found
done
kubectl delete deployment py-container
kubectl delete svc py-container py-container-nodeport --ignore-not-found


vnc:
kubectl delete svc vnc-desktop vnc-service
kubectl get all -A | grep -i vnc
kubectl delete deployment vnc-desktop

kubectl get pods -A --no-headers | awk '{print $1, $2, $4}' | sort | head

for x in py-container jenkins harbor-registry harbor-core rag; do
    echo
    echo "===== $x ====="
    kubectl get pods -A --no-headers | grep "$x" | \
        awk '{print $4}' | sort | uniq -c | sort -nr
done

# 1. Architecture
- IaaS, PaaS, SaaS (SW as a Service)
- k8s - Orchestration of aplication containers, developed by Google (in GoLang)
- Open-Source (Apache License)
- scalable - apps balancing - HA
- use dashboards, kubectl, REST API, controllers

- Control Plane
- Worker nodes
- kube-controller manager, cloud-controller manager
- kube scheduler
- kube-API server
- kubelet, kube-proxy (kubernetes nodes)
- etcd

- crictl
- ctr


### Basic Kubernetes components:
Control Plane:
    kube-apiserver
    kube-scheduler
    kube-controller-manager
    etcd
Node:
    kubelet
    kube-proxy
    Container Runtime

Additional tools:
    kubectl = CLI
    kubeadm = cluster installation/management tool
    runc = low-level runtime used by containerd/CRI-O
    crictl = talks to CRI/runtime

    runc alternatives:
        crun
        youki
        Kata Containers
        gVisor

    crictl alternatives:
        ctr
        nerdctl

HIGHER LEVEL
$ sudo crictl ps
CONTAINER   IMAGE        STATE
a1b2c3      nginx:1.27   Running

LOWER LEVEL
$ sudo runc list
ID          PID      STATUS
a1b2c3      1234     running

- runc list shows containers managed by the runc runtime.
- runc does NOT normally show image names.
- runc: Low-level runtime view Container ID, PID, status
- crictl understands: Pod + container + image
- runc understands: Container process + namespaces + cgroups
- crictl is specifically for CRI.
- runc is a low-level runtime.

Docker without Kubernetes:
docker CLI → Docker Engine → containerd → runc → container - crictl: NOT used.
runc: YES, normally used indirectly by Docker.
crictl is specifically for CRI.
runc is a low-level runtime.

Common Docker installation: Docker Engine-  containerd - runc - container
- runc IS normally installed as part of the Docker installation.

command -v runc
runc --version
sudo docker info | grep -i runtime
sudo docker info | grep -i containerd
sudo find /run -type f -name "state.json" 2>/dev/null | grep runc

- runc works with containers, not images.
- Images are managed by Docker/containerd.
Check running containers:
sudo runc --root /run/docker/runtime-runc/moby list

Your earlier "runc list" failed because runc was looking in /run/runc.
Docker uses: /run/docker/runtime-runc/moby/


### kubeam
- NOT a Kubernetes component.
- It is a tool for installing and managing a Kubernetes cluster.
Kubernetes components:
kube-apiserver
kube-scheduler
kube-controller-manager
kubelet
kube-proxy
etcd

crictl = Kubernetes/container-runtime tool. Use it when you are troubleshooting Kubernetes containers/pods.
ctr = containerd's low-level tool. Use it when crictl can't do something or you need to inspect/fix containerd directly.

crictl
- Belongs to Worker Nodes.
- Used to communicate with the container runtime through the CRI.
Worker node:
  kubelet
  kube-proxy
  container runtime
  crictl

### 1. etcd
- ETCD is a distributed reliable key-value store that is simple, secure & Fast.
- HTTP/JSON
- persistent cluster configuration

### 2. Controllers
- kube-controller-manager - runs containers
- Replication controller (replica-set)
- Endpoints controller - exposing services
- Service Account and Token controller - for accounts namespaces
- Cloud-controller manager, covers:
    - Node controller - checks of nodes availability
    - Route controller
    - Service controller
    - Volume controller

### 3. API Server
Main entry point to the Kubernetes cluster.
Receives kubectl/API requests.
Validates and stores cluster state.
Kubernetes API encryption

API Server uses TLS for communication.

Disable TLS:
  Not recommended.
  Requires changing API Server configuration and certificates.

Pod-to-Pod encryption:
  Not enabled by kubeadm by default.
  Controlled by the CNI.

### 4. kube-scheduler
- monitoring and scheduling start of containers kube-scheduler
- selects a suitable Worker Node for each Pod
- considers resources and WH/SW/Policy constraints.
Constraints
- Rules that limit where a Pod can run.
Examples:
CPU/memory
Node labels
Taints/tolerations

- Inter-workload - Scheduling Pods based on their relationship with other Pods
- Pod affinity: Run Pods together
- Pod anti-affinity: Keep Pods apart
- Deadlines (priorities)

### 5. kubelet
- Manages Pods assigned just by Kubernetes.
- Other containers started manually are managed by the container runtime, not by kubelet.
- Runs on every Kubernetes Node.
- Runs on every Worker Node.
- Worker Nodes: Manages Pods.
- Control Plane Nodes: Runs control plane Pods.
- Communicates with API Server.
- Ensures Pods and containers are running as requested.

### 6. kube-proxy
- network proxy
- Runs on every Kubernetes Node.
- Manages network rules.
- Enables communication to Services and Pods.
- use OS netfiltering (e.g. iptables, nftables)
- Modern Kubernetes networking may use nftables, iptables, IPVS, or eBPF, depending on the implementation.
- VIP (virtual address): in k8s Services use a Virtual IP (ClusterIP).
- kube-proxy: Implements Service VIP → Pod routing using iptables, IPVS, nftables, etc.
- VIF (Virtual Network Interface) - Not the mechanism kube-proxy uses to implement Service networking.
- VIF = general virtual network interface (networking concept) - not used in k8s
- VIP = virtual IP / Service ClusterIP
- kube-proxy = implements Service networking - Service networking is virtual.
- Service: Virtual IP (ClusterIP) but no physical network interface is created for the Service.
- kube-proxy / CNI: Implements the virtual Service IP using network rules or eBPF.
- VIP = virtual address
- VIF = virtual interface
- Service = virtual networking
- Sticky Session - Keeps a client connected to the same Pod across requests.
- Sticky Session - Useful when session state is stored locally in the Pod.

### 7. Container Runtime
- CRI = Container Runtime Interface. Communication interface. Kubernetes API/spec for talking to runtimes.
- CRI API/interface is used by kubelet
- CRI is the interface between kubelet and the container runtime.
- abstraction on top of OS
- sets cgroups, ns, chroot
- Container Runtimes examples:
containerd
Docker Engine
Mirantis Container Runtime
Kata Containers
gVisor
CRI-O

Flow: kubelet - CRI API - containerd - runc - container
ctr = CLI tool for containerd

CRI = a software API/specification, NOT a file. 
It defines the messages/functions that kubelet uses to ask a container runtime to:
  create a Pod sandbox
  create/start/stop containers
  remove containers
  report container status
  manage images

- kubeadm default: - containerd is NOT installed by kubeadm.
- You install a CRI runtime separately. Common choice: containerd
- Common kubeadm setup: kubelet → CRI → containerd → runc
- CRI-O is an alternative, not used by default, cmd to check:
systemctl status crio


# 2. Networking
- internal bridge - net interface docker
- routings - nat, firewall
- loadbalancer - external

# 3. Storage
- volumes - mount points

### namespaces
- OS level / k8s namespaces (resources limits)

### cgroups

### Image layers

Base layers = read-only
Top/container layer = read-write
- isolation - namespaces, mount ns, cgroups, chroot, processes, network ns (can be shared between pods)

### dockerd
dockerd
Docker daemon
- Manages images, containers, networks, and volumes.
- Runs in the background and listens for Docker API requests.
- can use docker compose
- Can work with container registries.
Pull images from registries.
Push images to registries.
Examples:
    Docker Hub
    GitHub Container Registry
    AWS ECR
    Google Artifact Registry
    Harbor

### Registry
- A registry = the whole image storage service.
- A registry can contain many repositories.
Other examples:
- Service registry - Stores information about available services.
- Package registry - Stores software packages. Example: npm registry.
- Container registry - Stores container images.

### Repository
- A repository = a collection of images inside a registry.

Example:
Docker Hub
  └── nginx repository
        ├── nginx:latest
        ├── nginx:1.27
        └── nginx:1.28

- In Kubernetes, you usually specify the registry + repository + image tag:
registry.example.com/myapp/backend:1.0

### Context
kubectl config use-context <context-name>

### SSL:

sudo kubeadm certs check-expiration
sudo ls -la /etc/kubernetes/pki/
sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
openssl s_client -connect <CONTROL_PLANE_IP>:6443
openssl s_client -connect <NODE_IP>:10250
sudo ls -la /etc/kubernetes/pki/etcd/
kubectl get pods -n kube-system -o wide

# Check certificate expiration
sudo kubeadm certs check-expiration

# List Kubernetes PKI certificates
sudo ls -la /etc/kubernetes/pki/

# Check API server certificate details
sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout

# Check certificate algorithm
sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -E "Signature Algorithm|Public Key Algorithm"

# Check TLS version on API server
openssl s_client -connect <CONTROL_PLANE_IP>:6443

# Check kubelet TLS
openssl s_client -connect <NODE_IP>:10250

# Check etcd certificates
sudo ls -la /etc/kubernetes/pki/etcd/

# Check CNI / node networking
kubectl get pods -n kube-system -o wide

# Check network traffic between nodes
sudo tcpdump -i any -nn host <OTHER_NODE_IP>