### BASIC CONCEPT

    - Kubernetes is a container orchestration platform
    - manages containerized applications
    - schedules containers
    - maintains desired state
    - provides service discovery
    - handles scaling
    - replaces failed workloads
    - supports rolling deployments


### CLUSTER

- A Kubernetes cluster consists of:

Control Plane:

1. API Server
2. etcd
3. Scheduler
4. Controller Manager

Worker Nodes:

1. Kubelet
2. Container Runtime
3. kube-proxy

### CONTROL PLANE

- The Control Plane manages the cluster.

Main components:

    1. API Server
    2. etcd
    3. Scheduler
    4. Controller Manager

### 1. API SERVER

- Main entry point to Kubernetes
- All communication with the cluster goes through the API Server
- kubectl communicates with the API Server
- handles:
    - Authentication
    - Authorization
    - Validation
    - API requests

Example:

    kubectl get pods
    kubectl apply
    kubectl delete


### 2. ETCD

- Distributed key value database
- Stores the Kubernetes cluster state
- Stores information about:
    - Pods
    - Deployments
    - Services
    - Secrets
    - ConfigMaps
    - Nodes
    - Cluster configuration

- Critical component of the Control Plane
- Should be backed up


### 3. SCHEDULER

- Decides which Worker Node should run a new Pod
- Checks:
    - CPU
    - Memory
    - Node availability
    - Taints
    - Tolerations
    - Node selectors
    - Affinity

- Assigns the Pod to a suitable Worker Node
- Does not run the container itself

### 4. CONTROLLER MANAGER

- Runs Kubernetes controllers
- Continuously compares
    - Desired state
    - Current state

- Tries to make the current state match the desired state
- Example:
    - Desired state
        - 3 replicas
    - Current state
        - 2 Pods
    - Controller creates another Pod


### WORKER NODE

- Worker Nodes run application workloads

Main components:

    1. Kubelet
    2. Container Runtime
    3. kube-proxy

### 1. KUBELET

- Agent running on every Worker Node
- Communicates with the API Server
- Ensures assigned Pods are running
- Reports Node and Pod status


### 2. CONTAINER RUNTIME

- Runs containers
- Examples:
    - containerd
    - CRI-O

- Kubernetes uses a container runtime to run containers


### 3. KUBE-PROXY

- Provides networking functionality for Services
- Helps route network traffic to the correct Pods


### POD

- Smallest deployable unit in Kubernetes
- Contains one or more containers
- Containers inside the same Pod share:
    - Network
    - IP address
    - Volumes

### KEY RELATIONSHIP

- Control Plane manages the cluster
- Worker Nodes run the workloads
- API Server is the main communication point
- etcd stores the cluster state
- Scheduler assigns Pods to Nodes
- Controller Manager maintains the desired state
- Kubelet manages Pods on Worker Nodes
- Container Runtime runs containers
- kube-proxy handles Service networking