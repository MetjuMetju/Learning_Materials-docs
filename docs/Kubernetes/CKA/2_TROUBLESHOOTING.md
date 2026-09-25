### TROUBLESHOOTING

### Troubleshoot clusters and nodes
    Pod Pending
    - Pod cannot be scheduled

    CrashLoopBackOff
    - container keeps crashing

    Node NotReady
    - node is not healthy/available

    kubelet
    - manages Pods on the node

    Events
    - show what went wrong

    describe
    - detailed information + events

### Troubleshoot cluster components
    API Server
    - handles Kubernetes API requests

    Scheduler
    - decides which node runs a Pod

    Controller Manager
    - maintains desired cluster state

    etcd
    - stores Kubernetes cluster data

    CoreDNS
    - provides cluster DNS

    kubelet
    - manages containers on each node

    containerd
    - runs containers

### Monitor cluster and application resource usage
    CPU
    - processor usage

    Memory
    - RAM usage

    Requests
    - resources guaranteed/reserved for a container

    Limits
    - maximum resources a container can use

    kubectl top
    - shows current CPU/memory usage

    kubectl describe
    - shows configured requests/limits

### Manage and evaluate container output streams

    kubectl logs
    - show container logs

    --previous
    - logs from previous crashed container

    -c <container>
    - select a specific container

    -f
    - follow logs continuously

    kubectl exec
    - run command inside a container

    describe
    - show container state/events

### Troubleshoot services and networking

    Service
    - provides stable access to Pods

    Selector
    - chooses which Pods receive traffic

    Endpoints
    - Pod IPs behind a Service

    ClusterIP
    - internal Service IP

    NodePort
    - exposes Service through a node port

    DNS
    - converts Service names to IPs

    NetworkPolicy
    - controls allowed network traffic

    Ingress
    - HTTP/HTTPS entry into the cluster

    Pod-to-Pod
    - direct communication between Pods