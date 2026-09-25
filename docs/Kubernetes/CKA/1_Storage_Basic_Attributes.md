### Storage — Basic Attributes

    accessModes
    - ReadWriteOnce (RWO)    - volume can be mounted read/write by one node
    - ReadOnlyMany (ROX)     - volume can be mounted read-only by many nodes
    - ReadWriteMany (RWX)    - volume can be mounted read/write by many nodes
    - ReadWriteOncePod (RWOP) - volume can be mounted read/write by one Pod

    persistentVolumeReclaimPolicy
    - Retain   - keep the PV/data after PVC is deleted
    - Delete   - delete the PV/storage when PVC is deleted
    - Recycle  - old/legacy option; scrub data and make PV available again

    capacity
    - storage: 1Gi   - amount of storage available

    storageClassName
    - name of the StorageClass used by the PVC/PV

    volumeMode
    - Filesystem - volume is mounted as a filesystem
    - Block      - volume is exposed as a raw block device

    hostPath
    - path: /mnt/data - directory on the node used for storage

### PVC — Basic Attributes

    resources.requests.storage
    - how much storage the PVC asks for

    accessModes
    - how the PVC wants to access the storage

    storageClassName
    - which StorageClass should provide the storage

    volumeName
    - explicitly select a specific PV

    status
    - Pending - not yet bound
    - Bound   - successfully connected to a PV
    - Lost    - PV is no longer available

### StorageClass — Basic Attributes
    provisioner
    - component that creates storage automatically

    reclaimPolicy
    - what happens to storage when PVC is deleted

    volumeBindingMode
    - Immediate            - provision storage immediately
    - WaitForFirstConsumer - wait until a Pod needs the PVC

    allowVolumeExpansion
    - true  - allow PVC to be expanded
    - false - cannot expand PVC