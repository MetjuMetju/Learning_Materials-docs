### TOPIC 5. SERVICES & NETWORKING - 20%

### QUESTION 1 - Create a Deployment named web and a Service named web-svc.

```code
# Requirements: 3 replicas
# Container image: nginx
# Create a Service named web-svc.
# Service type: ClusterIP
# Service port: 80
# Target port: 80
# The Service must route traffic to all three Pods.
# Then test the Service from inside the cluster.

# Create the Deployment.
kubectl create deployment web --image=nginx --replicas=3
kubectl get deployment web

# Check the Pods
kubectl get pods
# Wait until all three Pods are Running.

# Check the Pod labels
kubectl get pods --show-labels
# You should see the label:
app=web

# Create the Service.
kubectl expose deployment web --name=web-svc --port=80 --target-port=80 --type=ClusterIP
kubectl get svc web-svc

# Describe the Service.
kubectl describe svc web-svc

# Check:
Type
Selector
Port
TargetPort
Endpoints

# Check the endpoints directly.
kubectl get endpoints web-svc
# You should see the IP addresses of the three Pods.

# Check EndpointSlices
kubectl get endpointslices

# Create a temporary Pod for testing
kubectl run test-pod --image=busybox:1.36 --restart=Never -it --rm -- sh

# Inside the test Pod, test the Service.
wget -qO- http://web-svc
# You should receive nginx HTML output.

# Test the Service using its cluster DNS name.
wget -qO- http://web-svc.default.svc.cluster.local
# You should again receive nginx HTML output.

# Exit the test Pod
exit

# Check the Service again
kubectl get svc web-svc
kubectl get endpoints web-svc

# Clean up
kubectl delete service web-svc
kubectl delete deployment web


### IMPORTANT COMMANDS TO MEMORIZE
kubectl expose deployment NAME --name=SERVICE_NAME --port=80 --target-port=80
kubectl get svc
kubectl describe svc SERVICE_NAME
kubectl get endpoints SERVICE_NAME
kubectl get endpointslices
kubectl get pods --show-labels
kubectl run test-pod --image=busybox:1.36 --restart=Never -it --rm -- sh
wget -qO- http://SERVICE_NAME
```


### QUESTION 2 - Create a Deployment named backend.

```code
# Requirements: 3 replicas
# Image: nginx
# Create a NodePort Service named backend-svc.
# Service port: 80
# Target port: 80
# NodePort: 30080
# Verify that the Service selects all three Pods.

# Create Deployment
kubectl create deployment backend --image=nginx --replicas=3

# Check Pods
kubectl get pods --show-labels

# Create the Service
kubectl expose deployment backend --name=backend-svc --type=NodePort --port=80 --target-port=80

# Check the Service
kubectl get svc backend-svc

# Get the generated NodePort
kubectl describe svc backend-svc

# Edit the Service
kubectl edit svc backend-svc
# Find:
nodePort:
# Change the value to:
30080
# Save and exit.

# Verify:
kubectl get svc backend-svc
# You should see:
80:30080/TCP

# Check the selector
kubectl describe svc backend-svc


Check endpoints.

kubectl get endpoints backend-svc


You should see three Pod IP addresses.


STEP 10

Check EndpointSlices.

kubectl get endpointslices


STEP 11

Test from inside the cluster.

kubectl run test-pod --image=busybox:1.36 --restart=Never -it --rm -- sh


Inside:

wget -qO- http://backend-svc


You should receive nginx HTML.


Exit:

exit


STEP 12

Get the node IP.

kubectl get nodes -o wide


STEP 13

Test NodePort if your kind networking setup exposes it.

curl http://NODE_IP:30080


If kind does not expose the NodePort to your host, this is a limitation of the kind networking setup rather than necessarily a Kubernetes Service problem.


STEP 14

Final verification.

kubectl get deployment backend

kubectl get pods -o wide

kubectl get svc backend-svc

kubectl get endpoints backend-svc


# IMPORTANT CKA COMMANDS
kubectl expose
kubectl get svc
kubectl describe svc
kubectl get endpoints
kubectl get endpointslices
kubectl get pods --show-labels
kubectl run
```