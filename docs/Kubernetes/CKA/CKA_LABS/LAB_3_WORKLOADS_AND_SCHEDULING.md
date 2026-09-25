### TOPIC 3. WORKLOADS & SCHEDULING - 15%

### QUESTION 1:

```code
### Create a Deployment named frontend
### Requirements: 3 replicas
### Container image: nginx:1.25
### Then update the Deployment to: nginx:1.27
### Scale the Deployment to:
### 5 replicas
### Finally roll back to the previous image version.


# Create the Deployment
kubectl create deployment frontend --image=nginx:1.25 --replicas=3
kubectl get deployment frontend
kubectl get pods
# You should have 3 Pods.

# Check the current image
kubectl get deployment frontend -o wide

# You should see:
nginx:1.25

# Update the image.
kubectl set image deployment/frontend nginx=nginx:1.27

# Watch the rollout
kubectl rollout status deployment/frontend
# Wait until the rollout completes.

# Verify the image.
kubectl get deployment frontend -o wide

# Check rollout history.
kubectl rollout history deployment/frontend

# Scale the Deployment.
kubectl scale deployment frontend --replicas=5
kubectl get deployment frontend
kubectl get pods
# You should now have 5 Pods.


# Roll back the Deployment
kubectl rollout undo deployment/frontend

# Wait for the rollback
kubectl rollout status deployment/frontend
kubectl get deployment frontend -o wide
# The Deployment should now use:
nginx:1.25

# Check the final state
kubectl get deployment frontend
kubectl get pods
# You should have:
5 replicas
5 Pods Running

### COMMANDS TO MEMORIZE
kubectl create deployment NAME --image=IMAGE --replicas=NUMBER
kubectl get deployment
kubectl get pods
kubectl set image deployment/NAME CONTAINER=IMAGE
kubectl rollout status deployment/NAME
kubectl rollout history deployment/NAME
kubectl rollout undo deployment/NAME
kubectl scale deployment NAME --replicas=NUMBER
```

### QUESTION 2:

```code
### Create a Deployment named worker.
### Requirements:
### 3 replicas
### Image: nginx
### The Pods must run only on nodes labeled: workload=worker
### Your cluster currently has one node.
### Label the node appropriately.
### Then create the Deployment.
### Finally prevent new Pods from being scheduled onto the node and observe what happens.


# Check nodes
kubectl get nodes

# Label the node.
kubectl label node kind-control-plane workload=worker

# Verify
kubectl get nodes --show-labels

# Create the Deployment
kubectl create deployment worker --image=nginx --replicas=3

# Edit the Deployment
kubectl edit deployment worker

# Under:
spec:
  template:
    spec:

# add:
nodeSelector:
  workload: worker

# Save and exit.

# Check
kubectl get pods -o wide
# All Pods should be on the node labeled:
workload=worker


# Check the Deployment
kubectl get deployment worker

# Cordon the node
kubectl cordon kind-control-plane

# Verify
kubectl get nodes

# The node should show:
SchedulingDisabled

# Scale the Deployment
kubectl scale deployment worker --replicas=5

# Check
kubectl get pods -o wide
# Because the only node is cordoned, the additional Pods cannot be scheduled.

# Inspect one Pending Pod
kubectl describe pod POD_NAME
# Look at Events.

# Uncordon the node
kubectl uncordon kind-control-plane

# Check again
kubectl get pods -o wide
# The Pending Pods should now be scheduled.

# Final check
kubectl get deployment worker
kubectl get pods

# stop/remove pods:
kubectl scale deployment web --replicas=0


### IMPORTANT CKA COMMANDS
kubectl label node
kubectl get nodes --show-labels
kubectl cordon
kubectl uncordon
kubectl describe pod
kubectl scale deployment
```