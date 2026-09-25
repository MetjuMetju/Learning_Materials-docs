### WORKLOADS & SCHEDULING

### Deployments and rolling updates/rollbacks

    Deployment
    - manages and updates Pods

    ReplicaSet
    - maintains desired number of Pods

    Rolling update
    - gradually replaces old Pods

    Rollback
    - return to previous version

    Scale
    - increase/decrease Pod count

### ConfigMaps and Secrets

    ConfigMap
    - stores non-sensitive configuration

    Secret
    - stores sensitive data

    env
    - provide configuration as environment variables

    volume
    - mount ConfigMap/Secret as files

### Workload autoscaling
    HPA
    - automatically changes Pod count

    CPU
    - common HPA scaling metric

    minReplicas
    - minimum number of Pods

    maxReplicas
    - maximum number of Pods

    targetCPUUtilizationPercentage
    - CPU level that triggers scaling

### Robust, self-healing applications

    livenessProbe
    - checks if container is alive

    readinessProbe
    - checks if Pod is ready for traffic

    startupProbe
    - gives slow-starting applications time to start

    restartPolicy
    - controls container restart behavior

    replicas
    - multiple Pods for availability

### Pod admission and scheduling

    requests
    - resources needed for scheduling

    limits
    - maximum resources allowed

    nodeSelector
    - schedule Pod on nodes with specific labels

    nodeAffinity
    - more flexible node selection

    podAffinity
    - place Pods near other Pods

    podAntiAffinity
    - keep Pods away from other Pods

    taint
    - prevents Pods from being scheduled

    toleration
    - allows Pod to run on a tainted node