### CKA STUDY CHECKLIST

### 1. CLUSTER ARCHITECTURE
  Kubernetes components
  API Server
  etcd
  Scheduler
  Controller Manager
  kubelet
  Container runtime
  kube-proxy
  Control plane
  Worker nodes
  Kubernetes API
  Namespaces
  Contexts
  kubectl configuration
  kubectl config
  kubectl cluster-info
  kubectl api-resources
  kubectl api-versions
  kubectl explain

### 2. WORKLOADS

  Pod
  ReplicaSet
  Deployment
  DaemonSet
  StatefulSet
  Jobs
  CronJobs
  Labels
  Selectors
  Annotations
  Pod templates
  Scaling
  Rolling updates
  Rollbacks
  Deployment strategies
  kubectl rollout

### 3. SCHEDULING

Scheduling basics
nodeSelector
Node labels
Node affinity
Pod affinity
Pod anti-affinity
Taints
Tolerations
Cordon
Uncordon
Drain
Pod priority
Resource requests
Resource limits
CPU
Memory
Scheduling failures

### 4. STORAGE

Volumes
emptyDir
hostPath
PersistentVolume
PersistentVolumeClaim
StorageClass
Dynamic provisioning
Static provisioning
Access modes
ReadWriteOnce
ReadOnlyMany
ReadWriteMany
Reclaim policies
Retain
Delete
Volume binding
Immediate
WaitForFirstConsumer
Volume mounts
Storage troubleshooting

### 5. SERVICES AND NETWORKING
Service
ClusterIP
NodePort
LoadBalancer
Service selectors
Endpoints
EndpointSlices
Service ports
targetPort
port
nodePort
Cluster DNS
Service discovery
Pod networking
NetworkPolicy
Ingress
Ingress rules
Network troubleshooting

### 6. CONFIGURATION

ConfigMap
Secret
Environment variables
env
envFrom
ConfigMap volumes
Secret volumes
ImagePullSecrets
Security context

### 7. SECURITY
RBAC
Role
RoleBinding
ClusterRole
ClusterRoleBinding
ServiceAccount
Authorization
kubectl auth can-i
SecurityContext
runAsUser
runAsGroup
fsGroup
Privileged containers
Capabilities

### 8. TROUBLESHOOTING
Pod Pending
CrashLoopBackOff
ImagePullBackOff
ErrImagePull
ContainerCreating
FailedMount
FailedScheduling
Pod not Ready
Readiness probe
Liveness probe
Startup probe
Deployment failure
ReplicaSet failure
Service has no endpoints
Wrong Service selector
Wrong port
Wrong targetPort
DNS problems
NetworkPolicy problems
PVC Pending
PV problems
Node NotReady
kubelet problems
Container runtime problems
Resource problems
Events
Logs

### 9. PROBES
Liveness probe
Readiness probe
Startup probe
httpGet
tcpSocket
exec
initialDelaySeconds
periodSeconds
timeoutSeconds
failureThreshold
successThreshold

### 10. NETWORKING DETAILS
Pod IP
Service IP
Cluster DNS
CoreDNS
Service discovery
DNS names
NetworkPolicy ingress
NetworkPolicy egress
Namespace selectors
Pod selectors
Ingress

### 11. CONTAINER IMAGES
Container image
Image tag
ImagePullPolicy
ImagePullSecrets
Private registries
Container commands
command
args
Container ports

### 12. RESOURCE MANAGEMENT
Resource requests
Resource limits
CPU
Memory
LimitRange
ResourceQuota
QoS classes
Guaranteed
Burstable
BestEffort

### 13. YAML AND KUBECTL
apiVersion
kind
metadata
spec
metadata.name
metadata.namespace
labels
selectors
kubectl get
kubectl describe
kubectl create
kubectl apply
kubectl edit
kubectl delete
kubectl patch
kubectl replace
kubectl logs
kubectl exec
kubectl run
kubectl expose
kubectl scale
kubectl label
kubectl annotate
kubectl rollout
kubectl explain
kubectl diff
kubectl wait

### 14. JSONPATH AND OUTPUT
-o yaml
-o json
-o wide
-o name
-o jsonpath
Custom columns
Filtering resources
Sorting resources

### 15. CKA TROUBLESHOOTING WORKFLOW
kubectl get
kubectl describe
kubectl logs
kubectl logs --previous
kubectl get events --sort-by=.lastTimestamp
kubectl get RESOURCE NAME -o yaml


### 16. IMPORTANT RELATIONSHIPS
Deployment manages ReplicaSet.
ReplicaSet manages Pods.
Service selects Pods using labels.
Pod uses PVC.
PVC binds to PV.
StorageClass can dynamically provision PVs.
Ingress routes HTTP and HTTPS traffic.
NetworkPolicy controls Pod traffic.
ServiceAccount provides Pod identity.
Role and ClusterRole define permissions.
RoleBinding and ClusterRoleBinding grant permissions.

### 17. CKA PRACTICAL SKILLS
Create resources quickly.
Modify existing resources.
Find resources.
Filter resources.
Read YAML.
Generate YAML.
Edit YAML.
Scale workloads.
Perform rollouts.
Rollback deployments.
Schedule Pods.
Troubleshoot Pods.
Troubleshoot Services.
Troubleshoot storage.
Troubleshoot nodes.
Configure RBAC.
Configure NetworkPolicy.
Work with ConfigMaps.
Work with Secrets.
Work with persistent storage.
Use kubectl efficiently.
