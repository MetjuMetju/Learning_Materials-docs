### DAEMONSET

- A DaemonSet ensures that a Pod runs on every eligible node in the cluster.
- set 1 Pod per eligible node (no any replicas).

### Typical uses:

  Monitoring agents
  Log collectors
  Node agents
  Networking components


### CREATE A DAEMONSET
```code
vi daemonset.yaml

apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring
spec:
  selector:
    matchLabels:
      app: monitoring
  template:
    metadata:
      labels:
        app: monitoring
    spec:
      containers:
        - name: monitoring
          image: nginx


# CREATE IT
kubectl apply -f daemonset.yaml

# CHECK
kubectl get daemonset
kubectl get ds
kubectl get pods -o wide

# DaemonSet does not use:
replicas:
# Instead:
one Pod per eligible node

# IF CONTROL PLANE HAS A TAINT
# A normal DaemonSet may not run on a tainted control plane node.

# Check:
kubectl describe node NODE_NAME
# Look for:
Taints:

# To allow the DaemonSet onto that node:
tolerations:
  - key: node-role.kubernetes.io/control-plane
    operator: Exists
    effect: NoSchedule

# SCHEDULE ONLY ON SPECIFIC NODES
# Use nodeSelector:
nodeSelector:
  disk: ssd

# Then the DaemonSet runs only on nodes matching:
disk=ssd


### IMPORTANT COMMANDS
kubectl get ds
kubectl describe ds monitoring
kubectl get pods -o wide
kubectl delete ds monitoring


### CKA MEMORY
# Deployment:
desired number of Pods

# DaemonSet:
one Pod per eligible node

# StatefulSet:
stable identity and storage

# Job:
runs to completion

# CronJob:
runs on a schedule
```

### DAEMONSET PURPOSE

- Use a DaemonSet when you need the SAME Pod running on EVERY node.
- Think: "One agent per node."

```code

### EXAMPLE 1
# LOG COLLECTOR
# You want to collect logs from every Kubernetes node.
# Create a DaemonSet:

kind: DaemonSet
image: fluent-bit

# Result:
Node 1 -> fluent-bit Pod
Node 2 -> fluent-bit Pod
Node 3 -> fluent-bit Pod

# If you add Node 4: Kubernetes automatically creates a fluent-bit Pod on Node 4.

### EXAMPLE 2
# MONITORING AGENT
# You want a monitoring agent on every node.
# kind: DaemonSet
# image: prometheus-node-exporter
# Result: Every eligible node gets one monitoring Pod.


EXAMPLE 3

NODE NETWORK AGENT

A networking component needs to run on every node.

DaemonSet is appropriate because Kubernetes ensures
one Pod exists on each eligible node.


WHY NOT DEPLOYMENT?

Deployment:

"Give me 3 Pods."

DaemonSet:

"Give me 1 Pod on every eligible node."


CKA MEMORY

Deployment = number of replicas

DaemonSet = one per node

StatefulSet = stable identity

Job = finish a task

CronJob = run a task on a schedule