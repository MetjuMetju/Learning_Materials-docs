### Buildah official documentation:

        https://buildah.io/
        https://buildah.io/tutorials/

### Red Hat documentation:
        https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/building_running_and_managing_containers/assembly_building-container-images-with-buildah


### Buildah history:
- Buildah was created as part of the Red Hat / Project Atomic container ecosystem
- designed for building OCI container images without needing a Docker daemon

##### 2017
- Buildah first appeared as a new command-line tool for building OCI container images and containers, developed in the Red Hat / Project Atomic container ecosystem

##### 22 Jun 2017
- The first public Buildah introduction was published. The idea was to build container images without requiring a Docker daemon, making image building easier to script and automate

##### 2018
- Buildah continued to mature with Dockerfile support, image-layer control, rootless/user-namespace work, pull/push support, and other container-building features

##### 2019+
- Buildah became part of the broader containers ecosystem together with tools such as Podman and Skopeo, and continued developing as an OCI image-building tool

##### Today
- Buildah is maintained by the containers organization and is used to build, modify, inspect, and push OCI/container images, with or without a container runtime daemon

##### Official history:
        https://buildah.io/blogs/2017/06/22/introducing-buildah.html


### BUILDAH GUIDE

- The official Buildah documentation is mainly organized around commands and tutorials.

### CORE COMMANDS

        add
        build
        commit
        config
        containers
        copy
        from
        images
        inspect
        login
        mount
        pull
        push
        rm
        rmi
        run
        unmount
        tag
        unshare
        version

### TUTORIALS

        Introduction Tutorial
        Buildah and Registries Tutorial
        Buildah ONBUILD Tutorial
        Include Buildah in your build tool
        Rootless OpenShift container

### BUILDING IMAGES

        build
        Containerfile / Dockerfile
        build context
        FROM
        RUN
        COPY
        ADD
        ENV
        ARG
        CMD
        ENTRYPOINT
        USER
        WORKDIR
        EXPOSE
        LABEL
        VOLUME
        ONBUILD

##### IMAGE MANAGEMENT

        images
        inspect
        tag
        commit
        pull
        push
        rmi

### WORKING WITH CONTAINERS

        from
        containers
        run
        copy
        add
        mount
        unmount
        rm
        commit

### REGISTRIES

        login
        pull
        push
        authentication
        registry transports
        image names
        tags and digests

        ROOTLESS / ADVANCED

        rootless containers
        user namespaces
        unshare
        isolation
        OCI runtime
        storage
        layers
        build cache
        multi-stage builds
        multi-architecture builds
        secrets
        SSH mounts
        SBOM

### CONFIGURATION

        registries.conf
        policy.json
        containers.conf
        authentication files
        environment variables

### BUILDAH TOPICS

- 01  What is Buildah?
- 02  Buildah vs Docker vs Podman
- 03  Installation and setup

- 04  Images and Containerfiles
- 05  Building images
- 06  Image configuration
- 07  Image layers and build cache
- 08  Tags and digests
 
- 09  Container registries
- 10  Registry authentication and security
- 11  Pulling images
- 12  Pushing images
- 13  Image backup and layers
 
- 14  Containers and container lifecycle
- 15  buildah from
- 16  buildah run
- 17  buildah copy
- 18  buildah mount / unmount
- 19  buildah commit
- 20  Cleanup
 
- 21  Namespaces and isolation
- 22  Rootless Buildah
- 23  buildah unshare
 
- 24  Volumes and host data
- 25  Environment variables
- 26  Ports and networking
- 27  Security and permissions
 
- 28  Buildah scripting
- 29  Buildah and OCI
- 30  Buildah and Podman
- 31  Troubleshooting
- 32  Practical build workflow

### Buildah basics

### IMAGE

- An image is NOT stored as one single file. It is mainly represented by:

        manifest = describes the image and points to its content
        config   = image configuration
        layers   = filesystem changes
        blobs    = stored binary objects, usually layers/config/other content
        tag      = human-readable label like v1.2
        digest   = unique hash that identifies exact content

### REGISTRY

- A registry organizes and serves container image content through repositories and manifests.
- It mainly contains lists of manifests:

        repositories = namespaces for related image references
        manifests    = describe an image and reference its content
        image indexes = describe a set of platform-specific manifests
        blobs        = content referenced by manifests (layers, image config, etc.)
        tags         = names associated with manifests
        digests      = content-addressable identifiers for manifests/blobs
        config       = image configuration referenced by the manifest
        layers       = filesystem content referenced by the manifest

### ARTIFACT
- artifact = any piece of data produced, stored, or distributed by a registry

        Examples:

        image manifest = artifact
        image index    = artifact
        image config   = artifact
        image layer    = artifact

- In container registries:

        artifact = content that can be stored and referenced by a digest

- A registry can handle different OCI artifacts, for example:

        container image
        image index
        Helm chart
        SBOM
        signature
        attestation

### MANIFEST

- A manifest describes one container image and points to its content

```code
### Example:

{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "config": {
    "mediaType": "application/vnd.oci.image.config.v1+json",
    "digest": "sha256:abc123..."
  },
  "layers": [
    {
      "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
      "digest": "sha256:def456..."
    }
  ]
}
```

- In a MIME media type: application/vnd.oci.image.manifest.v1+json
- vnd means the format is vendor-specific rather than a standard generic format.
- oci = Open Container Initiative
- image.manifest = what the data represents
- v1 = version 1
- +json = the data is encoded as JSON
- so application/vnd.oci.image.manifest.v1+json
- means: JSON data containing an OCI image manifest, using the vendor-specific OCI media-type namespace

- The platform is normally described by an IMAGE INDEX:

        Examples:
        linux/amd64
        linux/arm64
        linux/arm/v7

- manifest    = describes one image
- image index = selects manifests for different platforms
- platform    = OS + architecture, e.g. linux/amd64

### Installation

##### On a typical Linux system:

        sudo apt install buildah

##### or on Fedora / RHEL-based systems:

        sudo dnf install buildah

##### After installation:

        buildah version
        buildah info


### REGISTRY vs REPOSITORY

- registry   = the server/service that stores and distributes container content
- repository = a named collection of images inside a registry

Example:
registry.example.com/myapp:1.0

registry   = registry.example.com
repository = myapp
tag        = 1.0

registry   = WHERE
repository = WHICH COLLECTION
image      = WHAT
tag        = WHICH VERSION/NAME
digest     = EXACT CONTENT

WHY DOCKER IS MORE WIDELY USED THAN BUILDAH?

Docker became popular first.

Docker:
- arrived early and became the default container tool
- has a very simple developer workflow
- includes build, run, network, volumes, registry, Compose, etc.
- has a huge ecosystem, documentation, tutorials, and community
- is what many developers first learn

Buildah:
- is mainly focused on BUILDING and MANAGING images
- does not try to be the complete "Docker experience"
- is commonly used behind the scenes in Linux / Red Hat environments
- is often used together with Podman and Skopeo

### PODMAN vs BUILDAH

- Podman = run and manage containers
- Buildah = build and modify images
- Skopeo = copy and inspect images between registries/storage

- A common Red Hat-style toolchain is:

        Buildah  -> build image
        Podman   -> run container
        Skopeo   -> move/copy image

- Docker has a much larger historical developer/user base.

- Podman is particularly strong in:

        - Red Hat / RHEL
        - OpenShift
        - rootless containers
        - daemonless container workflows
        - environments where Docker compatibility is not required
