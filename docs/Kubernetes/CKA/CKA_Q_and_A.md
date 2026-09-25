### CKA test Q and A:

https://www.examcert.app/exams/cka/free-practice-test/

### 1.
Get list of all pods in all namespaces and write it to file “/opt/pods-list.yaml”

A
kubectl get po –all-namespaces > /opt/pods-list.yaml
B
kubectl get po -n develop > /opt/pods-list.yaml
C
kubectl list po -n develop > /opt/pods-list.yaml
D
kubectl set po -n develop > /opt/pods-list.yaml

### Correct answer:
kubectl get po --all-namespaces > /opt/pods-list.yaml

### 2.
Check the history of deployment

A
kubectl rollout history deployment webapp
B
kubectl roll history deployment webapp
C
kubectl history rollout deployment webapp
D
kubectl history deployment webapp

### Correct answer:
kubectl rollout history deployment webapp


### 3.
Create a daemonset named “Prometheus-monitoring” using image=prom/Prometheus which runs in all the nodes in the cluster.

A
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: prometheus-monitoring
spec:
  selector:
    matchLabels:
      name: prometheus
  template:
    metadata:
      labels:
        name: prometheus
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers:
        - name: prometheus-container
          image: nginx

B
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: prometheus-monitoring
spec:
  selector:
    matchLabels:
      name: prometheus
  template:
    metadata:
      labels:
        name: prometheus
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers:
        - name: prometheus-container
          image: node

C
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: prometheus-monitoring
spec:
  selector:
    matchLabels:
      name: prometheus
  template:
    metadata:
      labels:
        name: prometheus
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers:
        - name: prometheus-container
          image: prom/prometheus

D
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: prometheus-monitoring
spec:
  selector:
    matchLabels:
      name: prometheus
  template:
    metadata:
      labels:
        name: prometheus
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers:
        - name: prometheus-container
          image: prom/prometheus


### Correct answer:
D.
kind must be DaemonSet
image must be prom/prometheus
A uses nginx
B uses node
C uses StatefulSet
D satisfies all requirements

DaemonSet means one Pod on each eligible node.

If control plane nodes have a NoSchedule taint,
the DaemonSet needs a matching toleration to run there.


### 4.
List all pods in the current namespace, with more details

A
kubectl get pods
B
kubectl get pods -o wide
C
kubectl status pods
D
kubectl get all

### Correct answer:
B.


### 5.
Evict all existing pods from a node-1 and make the node unschedulable for new pods.

A
kubectl get nodes
kubectl drain node-1
Verify:
kubectl get nodes
When you cordon a node, the status shows
SchedulingDisabled.

B
kubectl list nodes
kubectl clear node-1
kubectl cordon node-1
Verify:
kubectl get nodes
When you cordon a node, the status shows
SchedulingDisabled.

C
kubectl get nodes
kubectl delete node-1
Verify:
kubectl get nodes
When you cordon a node, the status shows
SchedulingDisabled.

D
kubectl get nodes
kubectl drain node-1
kubectl cordon node-1
Verify:
kubectl get nodes
When you cordon a node, the status shows
SchedulingDisabled.


### Correct answer:
D.
REASON
drain = evicts existing Pods
cordon = prevents new Pods
Therefore:
kubectl drain node-1
kubectl cordon node-1

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
### 3.
### Correct answer:

### 3.
### Correct answer:
