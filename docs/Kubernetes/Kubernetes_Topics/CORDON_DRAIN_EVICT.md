### CORDON, DRAIN AND EVICT

### This belongs to: WORKLOADS AND SCHEDULING


### EVICT

- Gracefully remove a Pod from a node.
- Kubernetes asks the Pod to terminate, so the workload can be moved or recreated somewhere else.

### Example:

    Pod is running on node-1.
    kubectl drain node-1
    The Pod is evicted from node-1.

- If the Pod belongs to a Deployment, the Deployment creates a replacement Pod on another available node.


### CORDON

- Cordon makes a node unschedulable.

    kubectl cordon node-1
    Existing Pods stay running.
    New Pods cannot be scheduled there.

### DRAIN

- Drain prepares a node for maintenance.

    kubectl drain node-1
    1. Makes the node unschedulable.
    2. Evicts existing Pods that can be evicted.


### UNCORDON

- Allows new Pods to be scheduled again.


### CKA COMMANDS

    Check:
    kubectl get nodes

    Cordon:
    kubectl cordon node-1

    Drain:
    kubectl drain node-1

```code
# If DaemonSet Pods cause a drain error:
kubectl drain node-1 --ignore-daemonsets

# If emptyDir data causes a drain error:
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data

# Allow scheduling again:
kubectl uncordon node-1


# IMPORTANT DIFFERENCE
# cordon: Existing Pods stay. New Pods are blocked.
# drain: Existing Pods are evicted. New Pods are blocked.
# uncordon: New Pods can be scheduled again.

### REAL CKA SCENARIO
# You need to perform maintenance on node-1.
# First:
kubectl drain node-1 --ignore-daemonsets

# Perform maintenance. Then:
kubectl uncordon node-1

# MEMORY
cordon = block
drain = empty
uncordon = allow
```