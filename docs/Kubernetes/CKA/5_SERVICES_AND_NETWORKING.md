### SERVICES & NETWORKING

### Connectivity between Pods

    Pod IP
    - IP address assigned to a Pod

    Pod-to-Pod
    - Pods can communicate over the cluster network

    CNI
    - provides Pod networking

    Service
    - stable access to a group of Pods

### Network Policies

    NetworkPolicy
    - controls network traffic

    Ingress
    - incoming traffic

    Egress
    - outgoing traffic

    podSelector
    - selects Pods

    namespaceSelector
    - selects namespaces

    ipBlock
    - selects IP ranges

    Allow
    - explicitly permit traffic

    Deny
    - traffic not allowed by policy

### Services and endpoints

    ClusterIP
    - internal cluster access

    NodePort
    - exposes Service on each node

    LoadBalancer
    - exposes Service through external load balancer

    selector
    - selects backend Pods

    Endpoints
    - IP/ports of backend Pods

### Gateway API

    GatewayClass
    - defines the Gateway implementation

    Gateway
    - entry point for network traffic

    HTTPRoute
    - defines HTTP routing rules

    Listener
    - defines port/protocol for traffic

### Ingress

    Ingress
    - defines HTTP/HTTPS routing

    Ingress Controller
    - implements Ingress rules

    host
    - domain name used for routing

    path
    - URL path used for routing

    backend
    - Service receiving traffic

### CoreDNS
    CoreDNS
    - Kubernetes DNS server

    Service DNS
    - resolves Service names to IPs

    kubernetes.default
    - default Kubernetes API Service DNS name

    /etc/resolv.conf
    - tells Pod which DNS server to use

    kube-dns
    - Service exposing CoreDNS

    nslookup
    - tests DNS resolution