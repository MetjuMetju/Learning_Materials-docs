# CKA hands-on labs

### TOPICS:
##### 1. STORAGE - 10%
##### 2. TROUBLESHOOTING - 30%
##### 3. WORKLOADS & SCHEDULING - 15%
##### 4. CLUSTER ARCHITECTURE, INSTALLATION & CONFIGURATION - 25%
##### 5. SERVICES & NETWORKING - 20%

##### 1. STORAGE - 10%

    LAB 01 - Create and use a PVC
    LAB 02 - Create a PersistentVolume
    LAB 03 - Bind PV and PVC
    LAB 04 - StorageClass and dynamic provisioning
    LAB 05 - Access modes and reclaim policies
    LAB 06 - Use PVC in a Pod
    LAB 07 - Troubleshoot Pending PVC
    LAB 08 - Troubleshoot volume mount problems


##### 2. TROUBLESHOOTING - 30%

    LAB 09  - Troubleshoot a Pending Pod
    LAB 10  - Troubleshoot a CrashLoopBackOff Pod
    LAB 11  - Troubleshoot a failing Deployment
    LAB 12  - Troubleshoot node NotReady
    LAB 13  - Troubleshoot kubelet
    LAB 14  - Troubleshoot control-plane components
    LAB 15  - Troubleshoot Service connectivity
    LAB 16  - Troubleshoot DNS
    LAB 17  - Troubleshoot NetworkPolicy
    LAB 18  - Inspect logs and container output
    LAB 19  - Check CPU/memory resource usage
    LAB 20  - Troubleshoot application networking


##### 3. WORKLOADS & SCHEDULING - 15%

    LAB 21 - Create a Deployment
    LAB 22 - Perform a rolling update
    LAB 23 - Roll back a Deployment
    LAB 24 - Scale a Deployment
    LAB 25 - Create and use a ConfigMap
    LAB 26 - Create and use a Secret
    LAB 27 - Configure resource requests and limits
    LAB 28 - Configure liveness/readiness probes
    LAB 29 - Configure Pod autoscaling
    LAB 30 - NodeSelector
    LAB 31 - Node affinity
    LAB 32 - Pod affinity / anti-affinity
    LAB 33 - Taints and tolerations
    LAB 34 - Pod scheduling troubleshooting


##### 4. CLUSTER ARCHITECTURE, INSTALLATION & CONFIGURATION - 25%

    LAB 35 - RBAC: Role + RoleBinding
    LAB 36 - RBAC: ClusterRole + ClusterRoleBinding
    LAB 37 - ServiceAccount permissions
    LAB 38 - kubeadm cluster initialization
    LAB 39 - Join a worker node
    LAB 40 - Upgrade a Kubernetes cluster
    LAB 41 - Drain and uncordon a node
    LAB 42 - Backup etcd
    LAB 43 - Restore etcd
    LAB 44 - Control-plane troubleshooting
    LAB 45 - Highly available control plane concepts
    LAB 46 - Install/configure a CNI
    LAB 47 - Understand CRI/CNI/CSI
    LAB 48 - Helm installation and usage
    LAB 49 - Kustomize
    LAB 50 - CRDs
    LAB 51 - Operators


##### 5. SERVICES & NETWORKING - 20%

    LAB 52 - Create a ClusterIP Service
    LAB 53 - Create a NodePort Service
    LAB 54 - Create a LoadBalancer Service
    LAB 55 - Service selectors and endpoints
    LAB 56 - Debug Service connectivity
    LAB 57 - NetworkPolicy: allow traffic
    LAB 58 - NetworkPolicy: deny traffic
    LAB 59 - NetworkPolicy: namespace rules
    LAB 60 - Ingress
    LAB 61 - Ingress troubleshooting
    LAB 62 - Gateway API
    LAB 63 - CoreDNS
    LAB 64 - DNS troubleshooting
    LAB 65 - Pod-to-Pod networking



##### COMMON YAML FILES NAMES
```code
- pod.yaml
- deployment.yaml
- service.yaml
- pvc.yaml
- pv.yaml
- storageclass.yaml
- rbac.yaml
- networkpolicy.yaml
- ingress.yaml
- gateway.yaml
- kustomization.yaml
```
- Reuse/edit these files between labs.
