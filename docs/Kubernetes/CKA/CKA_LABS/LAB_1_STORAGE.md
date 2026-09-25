### TOPIC 1. STORAGE - 10%

### QUESTION 1 - Create a PersistentVolume

Create a PersistentVolume named pv01 with the following requirements:
Capacity must be 1Gi
Access mode must be ReadWriteOnce
Storage class must be manual
Use host path /data/pv01

```code

### CREATE THE PERSISTENT VOLUME

# Enter the node:
docker exec -it kind-control-plane bash
mkdir -p /data/pv01
exit

# Create file:
vi pv01.yaml

apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv01
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  hostPath:
    path: /data/pv01

# Apply it
kubectl apply -f pv01.yaml
kubectl get pv
```

### QUESTION 2 - CREATE THE PVC

```code
# Create a file
vi pvc01.yaml

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc01
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  resources:
    requests:
      storage: 500Mi

# Apply it
kubectl apply -f pvc01.yaml
kubectl get pvc

# Check both
kubectl get pv
kubectl get pvc

# The PV should now show Bound.
# The PVC should now show Bound.

# Important CKA concept
# PV capacity is 1Gi.
# PVC requests 500Mi.
# The PVC can bind to the 1Gi PV because the PV has enough capacity.
# PV = provides storage
# PVC = claims storage
# Pod = consumes the claim
```

### QUESTION 3 - CREATE THE POD WITH STORAGE

```code
# Create a file
vi storage-pod.yaml

apiVersion: v1
kind: Pod
metadata:
  name: storage-pod
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - name: storage
          mountPath: /mnt/data
  volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: pvc01

# Create the Pod
kubectl apply -f storage-pod.yaml
kubectl get pods

# Wait until you see
storage-pod   1/1   Running

### Verify the volume is mounted
kubectl describe pod storage-pod

# You should find
/mnt/data

# WRITE DATA TO THE PVC
kubectl exec storage-pod -- sh -c "echo hello > /mnt/data/test.txt"

# Read the file
kubectl exec storage-pod -- cat /mnt/data/test.txt

### VERIFY THE DATA IS REALLY ON THE PV

# Check the file from inside the kind node.
docker exec kind-control-plane ls -l /data/pv01
docker exec kind-control-plane cat /data/pv01/test.txt

### test persistence

# Delete the Pod
kubectl delete pod storage-pod
kubectl get pods

# The Pod should be gone.

# Create it again
kubectl apply -f storage-pod.yaml

# Wait
kubectl get pods

# When Running, check the file again
kubectl exec storage-pod -- cat /mnt/data/test.txt

# This proves that the data belongs to the persistent volume and not merely to the original Pod.

### CHECK EVERYTHING
# Run these commands

kubectl get pv
kubectl get pvc
kubectl get pods
kubectl describe pv pv01
kubectl describe pvc pvc01
kubectl describe pod storage-pod
kubectl exec storage-pod -- df -h /mnt/data
kubectl exec storage-pod -- ls -la /mnt/data

### CLEAN THE LAB
kubectl delete pod storage-pod
kubectl delete pvc pvc01
kubectl delete pv pv01

# Remove the directory from the kind node
docker exec kind-control-plane rm -rf /data/pv01

# Verify
kubectl get pv
kubectl get pvc
kubectl get pods

### MOST IMPORTANT COMMANDS TO MEMORIZE

kubectl get pv
kubectl get pvc
kubectl describe pv pv01
kubectl describe pvc pvc01
kubectl get pods
kubectl describe pod storage-pod
kubectl exec storage-pod -- sh
kubectl exec storage-pod -- cat /mnt/data/test.txt
kubectl apply -f FILE.yaml
kubectl delete -f FILE.yaml

### The required order is:
PV first
PVC second
Pod third
exec into Pod fourth
```
