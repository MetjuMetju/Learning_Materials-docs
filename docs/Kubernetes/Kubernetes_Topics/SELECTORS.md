### SELECTORS IN KUBERNETES

There are different selectors for different purposes.

### 1. nodeSelector
- Used by a Pod to choose which node should run it.

### Example:

    spec:
    nodeSelector:
        disk: ssd

Check it with:

    kubectl describe pod POD_NAME

Look for:

    Node-Selectors:

If you see:

    Node-Selectors: <none>

that simply means the Pod has no nodeSelector (that is completely normal).

### 2. Service selector

Used by a Service to find Pods.

### Example:

    spec:
    selector:
        app: web

The Service looks for Pods having:

    app=web

Check the Service with:

    kubectl describe svc SERVICE_NAME

Look for:

    Selector:

### Example:

    Selector: app=web


### 3. Deployment selector

- Used by a Deployment to identify the Pods it manages.

### Example:

    spec:
    selector:
        matchLabels:
        app: web

The Deployment manages Pods with:

    app=web


### VERY IMPORTANT CKA DISTINCTION

If the question says: Run the Pod on a node with label disk=ssd
You need:

    nodeSelector


If the question says: Make the Service send traffic to the Pods

You need:

    Service selector


If the question says: Deployment must manage these Pods

You need:

    Deployment selector


### Deployment:
-  selector is created automatically when you create it with kubectl create deployment — e.g. app=web.

### Service:
- selector is created only if you specify it or use kubectl expose deployment, which automatically copies the Deployment's Pod label as the Service selector.

### Pod:
- no Service-style selector is created; nodeSelector exists only if you specify it.

### Pod labels:
- are what a Service selector matches against.

<br>

### PRACTICE:
```code

# Create a Deployment:
kubectl create deployment web --image=nginx --replicas=3

# Check its labels:

kubectl get pods --show-labels
# You should see something like:
app=web

kubectl get deployment web -o yaml
# Look for:
spec:
  selector:
    matchLabels:
      app: web
# And:
spec:
  template:
    metadata:
      labels:
        app: web

# Now create a Service:
kubectl expose deployment web --name=web-svc --port=80 --target-port=80

# Check:
kubectl describe svc web-svc

# Look for:
Selector: app=web

# Then:
kubectl get endpoints web-svc
# You should see the three Pod IP addresses.

### MEMORY RULE
# Pod -> nodeSelector -> chooses a node
# Service -> selector -> chooses Pods
# Deployment -> selector -> manages Pods
```