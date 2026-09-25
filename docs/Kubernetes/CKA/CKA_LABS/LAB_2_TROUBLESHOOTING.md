### TOPIC 2. TROUBLESHOOTING - 30%

### QUESTION 1:

```code
# A Pod named pending-pod exists but is not starting. Find the reason and fix the problem.
# The Pod must become Running.

# Check the Pod
kubectl get pod pending-pod

# Get more information
kubectl describe pod pending-pod

# Look at the Events section, you may see a message such as:
Insufficient cpu
Insufficient memory
No nodes are available
node selector mismatch
taint

# Check the nodes
kubectl get nodes
kubectl get nodes -o wide

# Check node labels
kubectl get nodes --show-labels

# Check node taints
kubectl describe node NODE_NAME

# Look for:
Taints

# Check scheduling events
kubectl get events --sort-by=.lastTimestamp

# If the problem is a node selector, inspect the Pod
kubectl get pod pending-pod -o yaml
# Look for:
nodeSelector

# If the node has the wrong label, fix the label
kubectl label node NODE_NAME disk=ssd --overwrite

# Check the Pod again
kubectl get pod pending-pod

# If the problem is a taint, inspect it
kubectl describe node NODE_NAME
# Then determine whether the Pod needs a toleration or whether the taint should be removed.

# Verify
kubectl get pod pending-pod -o wide

# When a Pod is Pending:
kubectl describe pod POD_NAME
# is usually your first important command. Always read Events.
```


### QUESTION 2:

```code
### A Deployment named payments has 3 replicas.
### The Pods are not Ready.
### A Service named payments-svc exists.
### Find and fix the problem.
### Do not delete the Deployment.
### Do not recreate the cluster.

# Start with:
kubectl get deployment payments
kubectl get pods
kubectl get svc payments-svc

# Check the Pods
kubectl get pods -o wide

# Describe one unhealthy Pod
kubectl describe pod POD_NAME

# Check the logs
kubectl logs POD_NAME

# Check previous logs if necessary
kubectl logs POD_NAME --previous


# Check Deployment configuration
kubectl describe deployment payments

# Check the ReplicaSets
kubectl get rs

# Check recent events
kubectl get events --sort-by=.lastTimestamp

# Check the Service
kubectl describe svc payments-svc

# Check endpoints
kubectl get endpoints payments-svc

# Check labels
kubectl get pods --show-labels

# Find the actual problem. Possible causes include:
Wrong image
Wrong container command
Wrong readiness probe
Wrong Service selector
Wrong targetPort
Missing configuration
Failed volume mount

# Fix the actual problem. Use the appropriate command.
# For example:
kubectl set image deployment/payments CONTAINER_NAME=IMAGE

# or:
kubectl edit deployment payments
# or:
kubectl edit svc payments-svc

# Verify:
kubectl rollout status deployment/payments
kubectl get pods
kubectl get endpoints payments-svc


# FINAL STATE
3 replicas
3 Ready Pods

# Service has endpoints
```