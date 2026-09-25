### SERVICE MESH

- A service mesh manages communication between services inside a Kubernetes cluster.
- It can provide:
    Traffic control
    Service-to-service security
    Encryption
    Retries
    Timeouts
    Load balancing
    Observability
    Without changing application code.


- A service mesh commonly uses a proxy alongside each application Pod.

- COMMON EXAMPLES
    Istio
    Linkerd


- Service mesh is NOT the same as a Kubernetes Service.
- Service mesh: Adds advanced control and security to service-to-service communication.


### ADMISSION CONTROLLERS

- An admission controller is part of the Kubernetes API request process.
- It can inspect or modify a request before the resource is stored in etcd.
- REQUEST FLOW
    kubectl
    API Server
    Authentication
    Authorization
    Admission Control
    etcd

### TWO TYPES

- Mutating admission controller
    - Can MODIFY a request.
    - Example: Automatically add a sidecar container.

- Validating admission controller Can ACCEPT or REJECT a request.
    - Example: Reject a Pod that violates a security rule.


EXAMPLE
    kubectl apply -f pod.yaml

- The API Server receives the request.
- An admission controller checks it.
- If valid: Request is accepted.
- If invalid: Request is rejected.

EXAMPLES

    NamespaceLifecycle
    ResourceQuota
    ServiceAccount
    LimitRanger
    MutatingAdmissionWebhook
    ValidatingAdmissionWebhook

- WEBHOOKS

    - MutatingWebhookConfiguration - can modify resources.
    - ValidatingWebhookConfiguration - can accept or reject resources.


List admission-related resources:

    kubectl api-resources | grep -i admission

Check API Server admission configuration on a cluster where you have control-plane access:

    ps aux | grep kube-apiserver

Look for:

    enable-admission-plugins
    disable-admission-plugins

Check webhook configurations:
    kubectl get mutatingwebhookconfiguration
    kubectl get validatingwebhookconfiguration


- Admission controller: Controls requests going INTO the cluster.
- NetworkPolicy: Controls network traffic BETWEEN Pods.
- RBAC: Controls WHO is allowed to perform an action.

Terms:

- Admission = check or change API requests
- Mutating = modify
- Validating = accept or reject