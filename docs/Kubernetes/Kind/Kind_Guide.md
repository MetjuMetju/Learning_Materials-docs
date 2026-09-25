### Kind Guide

### Installation steps
```code
# for RedHat

uname -m
x86_64

sudo dnf install -y curl
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.33.0/kind-linux-amd64

chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind version

kind create cluster

kind get clusters
kind

kubectl get nodes
NAME                 STATUS   ROLES           AGE     VERSION
kind-control-plane   Ready    control-plane   4m55s   v1.37.0

# Enter the node
docker exec -it kind-control-plane bash
```

### KIND CLUSTER STOP AND START

```code

# To stop the entire kind cluster:
docker stop kind-control-plane

# To start it again:
docker start kind-control-plane

# Then verify:
kubectl get nodes


# This works for your current single-node kind cluster.
# If you have multiple kind nodes, stop/start all of them:
docker ps -a --filter "name=kind-"

# Then:
docker stop kind-control-plane
docker start kind-control-plane

# Do not use:
kind delete cluster
# unless you want to DESTROY the cluster.

kind delete cluster
# means: delete the entire cluster and its state.

```