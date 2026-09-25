### CLUSTER ARCHITECTURE, INSTALLATION & CONFIGURATION

### RBAC

    Role
    - permissions inside one namespace

    RoleBinding
    - gives Role permissions to a user/ServiceAccount

    ClusterRole
    - cluster-wide permissions

    ClusterRoleBinding
    - gives ClusterRole permissions cluster-wide

    ServiceAccount
    - identity used by Pods

    kubectl auth can-i
    - checks whether an action is allowed

### Prepare infrastructure

    CPU/RAM
    - resources required by nodes

    container runtime
    - runs containers

    kubelet
    - manages Pods

    network
    - nodes must communicate

    swap
    - normally disabled for Kubernetes nodes

### kubeadm clusters

    kubeadm init
    - creates control plane

    kubeadm join
    - adds node to cluster

    kubeadm token
    - manages join tokens

    kubeadm reset
    - removes kubeadm cluster configuration

### Cluster lifecycle
    upgrade
    - update Kubernetes version

    drain
    - safely move Pods away from node

    uncordon
    - allow scheduling on node again

    cordon
    - stop new Pods from being scheduled

### Highly available control plane

    HA
    - multiple control-plane nodes

    API Server
    - multiple instances for availability

    etcd
    - replicated cluster database

    load balancer
    - distributes API Server traffic

    quorum
    - majority of etcd members required

### Helm and Kustomize
    Helm
    - Kubernetes package manager

    Chart
    - packaged Kubernetes application

    helm install
    - install a chart

    helm upgrade
    - update a release

    Kustomize
    - customize Kubernetes YAML

    kubectl apply -k
    - apply Kustomize configuration

### Extension interfaces
    CRI
    - container runtime interface

    CNI
    - container networking interface

    CSI
    - container storage interface

    CRI
    - connects Kubernetes to container runtime

    CNI
    - provides Pod networking

    CSI
    - provides storage

### CRDs and Operators
    CRD
    - creates a new Kubernetes resource type

    Custom Resource
    - object created from a CRD

    Operator
    - automates management of an application

    Controller
    - watches resources and maintains desired state