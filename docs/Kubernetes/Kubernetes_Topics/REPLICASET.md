### REPLICASET

- A ReplicaSet makes sure that a specified number of Pod replicas are running.

### Example:

    replicas: 3

- means Kubernetes tries to keep 3 matching Pods running.
- normally you create a Deployment instead of creating a ReplicaSet directly.
- Deployment manages ReplicaSet.
- ReplicaSet manages Pods.


### CREATE A REPLICASET
```code

# Create:
vi rs.yaml

apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: nginx
          image: nginx

# Apply:
kubectl apply -f rs.yaml

# CHeck:
kubectl get rs
kubectl get pods
kubectl get rs web-rs -o wide

# The ReplicaSet selector:
app: web

# must match the Pod template label:
app: web

# SCALE REPLICASET
kubectl scale rs web-rs --replicas=5

# Check:
kubectl get rs
kubectl get pods

# DELETE ONE POD
kubectl delete pod POD_NAME

# Then:
kubectl get pods

# The ReplicaSet creates a replacement Pod.


# DELETE REPLICASET
kubectl delete rs web-rs

# The Pods managed by it are normally deleted too.

# TROUBLESHOOTING REPLICASET
kubectl get rs
kubectl describe rs web-rs
kubectl get pods --show-labels
kubectl get events --sort-by=.lastTimestamp

# CKA IMPORTANT
# Deployment: manages ReplicaSet
# ReplicaSet: manages Pods
# ReplicaSet selector: selects the Pods it manages
# Pod template: defines the Pods that should exist

### IMPORTANT COMMANDS
kubectl get rs
kubectl describe rs NAME
kubectl scale rs NAME --replicas=NUMBER
kubectl get rs -o yaml
kubectl get pods --show-labels
```