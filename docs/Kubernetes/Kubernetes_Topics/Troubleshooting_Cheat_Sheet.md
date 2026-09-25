# Troubleshooting Cheat Sheet
```code
kubectl get pods -A -o wide
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl logs <pod> -c <container>
kubectl get deployment
kubectl describe deployment <deployment>
kubectl rollout status deployment/<deployment>
kubectl rollout undo deployment/<deployment>
kubectl get nodes
kubectl describe node <node>
kubectl get svc,endpoints
kubectl describe svc <service>
kubectl get endpointslices
kubectl get networkpolicy -A
kubectl describe networkpolicy <policy>
kubectl top nodes
kubectl top pods -A
kubectl get pods -n kube-system -o wide
kubectl logs -n kube-system <pod>
kubectl run test --rm -it --image=busybox:1.36 -- sh

# on a node:
systemctl status kubelet
journalctl -u kubelet --no-pager -n 100
systemctl status containerd
sudo ls /etc/kubernetes/manifests/

--rm        - delete temporary Pod after exit
-it         - interactive terminal
-i          - keep stdin open
-t          - allocate terminal
--image     - specify container image
--          - command after this runs inside
-o wide     - show extra information, especially node/IP
-A          - all namespaces
-n          - namespace
-l          - label selector
-f          - follow/watch output
--previous  - logs from previous crashed container
```