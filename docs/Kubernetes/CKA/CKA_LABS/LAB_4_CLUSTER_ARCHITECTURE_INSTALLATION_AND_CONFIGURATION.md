##### TOPIC 4. CLUSTER ARCHITECTURE, INSTALLATION & CONFIGURATION - 25%

### QUESTION 1:

```code
### Create a namespace named cka.
### Create a Pod named nginx in namespace cka.
### Configure the current kubectl context so that cka becomes the default namespace.
### Then inspect the cluster configuration.

# Create the namespace
kubectl create namespace cka

# Create the Pod in the namespace
kubectl run nginx -n cka --image=nginx
kubectl get pods -n cka

# Check the current context
kubectl config current-context

# Check all contexts
kubectl config get-contexts

# Set cka as the default namespace for the current context
kubectl config set-context --current --namespace=cka

# Test it
kubectl get pods
# You should see the nginx Pod without using:
-n cka

# Verify the configuration
kubectl config view --minify
# Look for:
namespace: cka

# Inspect the cluster
kubectl cluster-info
kubectl get nodes
kubectl get nodes -o wide

# Inspect the node
kubectl describe node kind-control-plane

# Find available Kubernetes resources
kubectl api-resources

# Find available API versions
kubectl api-versions

# Practice Kubernetes documentation from the command line
kubectl explain pod
kubectl explain pod.spec
kubectl explain pod.spec.containers
kubectl explain deployment.spec

# Check the Pod YAML
kubectl get pod nginx -o yaml

# Clean up
kubectl delete namespace cka

### COMMANDS TO MEMORIZE
kubectl config current-context
kubectl config get-contexts
kubectl config use-context CONTEXT
kubectl config set-context --current --namespace=NAMESPACE
kubectl cluster-info
kubectl get nodes
kubectl describe node NODE_NAME
kubectl api-resources
kubectl api-versions
kubectl explain RESOURCE
kubectl get RESOURCE NAME -o yaml
```


### QUESTION 2:

```code
### Create a namespace named production.
### Configure the current kubectl context to use production.
### Create a Deployment named web with 2 replicas in that namespace.
### Then inspect the Kubernetes API and resource definitions.

# Create namespace
kubectl create namespace production

# Set the current namespace
kubectl config set-context --current --namespace=production

# Create Deployment
kubectl create deployment web --image=nginx --replicas=2

# Verify without using -n
kubectl get deployment
kubectl get pods

# Check the current context
kubectl config current-context

# Check context configuration
kubectl config view --minify

# Find information about Deployments
kubectl explain deployment

# Find Deployment specification fields
kubectl explain deployment.spec

# Find Pod specification fields
kubectl explain pod.spec

# List API resources
kubectl api-resources

# List API versions
kubectl api-versions

# Inspect the Deployment YAML
kubectl get deployment web -o yaml

# Inspect the Pods
kubectl get pods -o wide

# Inspect the node
kubectl describe node kind-control-plane

# Check cluster information
kubectl cluster-info

# Return the current context to default namespace
kubectl config set-context --current --namespace=default

# Verify
kubectl config view --minify

# Clean up
kubectl delete namespace production

### IMPORTANT CKA CONCEPT
# You should be comfortable moving between:
cluster
context
namespace
resource
Pod
node
API resource
resource specification
```