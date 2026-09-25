### BuildKit builder

- Docker's modern build engine
- Docker 18.06 - July 2018 - BuildKit appeared as an experimental builder backend.
- Docker 18.09 - BuildKit could be used without experimental mode and gained several important capabilities, including build secrets and cache garbage-collection configuration.
- Docker 23.0 - February 2023 - For Linux images, Docker made BuildKit + Buildx the default, and docker build became effectively an alias to the Buildx build functionality.
- usues instruction to the Dockerfile frontend

```code
# Docker CLI
docker build -t myapp:1.0 .
docker push registry/myapp:1.0

# BuildKit directly
buildctl build \
  --frontend=dockerfile.v0 \
  --local context=. \
  --local dockerfile=. \
  --output type=image,name=registry/myapp:1.0,push=true

# modern docker build itself uses BuildKit underneath
# A frontend converts a human-readable build definition (Dockerfile)
# into BuildKit's internal LLB (Low-Level Build) build instructions.

# syntax=docker/dockerfile:1
# means essentially: "Use this Dockerfile syntax/frontend to interpret the following file."
# alts:
# syntax=docker/dockerfile:1.7
# syntax=docker/dockerfile:1.4
# The :1 form is generally preferable because it tracks the latest compatible v1 syntax rather than pinning an old minor version.
# There are also third-party/custom frontends, because BuildKit's frontend mechanism isn't limited to Dockerfile syntax.
# The frontend can come from an image, e.g. conceptually:
# syntax=<some-frontend-image>
```

### Commands:

```code
docker version

# shows Docker's disk usage
docker buildx du --verbose

# Inspect the build cache and records (refferences)
docker system df
docker system df -v
```

### Simplest explicit OCI output
```code
docker buildx build \
  --output type=oci,dest=myapp.tar \
  -t myapp:1.0 .

# or cmd:
docker buildx build --output type=oci,dest=./image.tar .
```

https://docs.docker.com/build/exporters

- Exporters are BuildKit's way of choosing how/where the build result is delivered (Docker image, OCI image, local files, tarball, etc.), because the same build result may need different formats/destinations for different consumers.

docker buildx build
- type=image - push/use as container image
- type=oci - create OCI image archive
- type=docker - create Docker image archive
- type=local - export files to a directory
- type=tar - export filesystem as tar

OCI - open, vendor-neutral standard; useful when you want maximum interoperability between container tools.
Docker - Docker's image/archive format; useful for Docker-specific workflows and compatibility.
Local - not really an image; exports build output as ordinary files.
Tar - useful when you need a portable archive/filesystem rather than a registry image.


### A legacy Docker Schema 1 image:
```code
image: ubuntu:10.04
format: Docker Image v1 / Schema 1

docker pull ubuntu:10.04
Error:
Docker Image Format v1 and Docker Image manifest version 2,
schema 1 support has been removed.

# Docker removed Schema 1 support in Docker 28.2.
# Current containerd recommends migrating it to Docker Schema 2 or OCI

# fix it - rebuild the application/image using a modern Dockerfile:
FROM ubuntu:24.04
COPY app /app
CMD ["/app"]

# Then:
docker build -t registry.example.com/myapp:1.0 .
docker push registry.example.com/myapp:1.0

# Command:
docker image inspect myapp:1.0  # inspect the IMAGE you have locally
docker manifest inspect myregistry/myapp:1.0        # inspect the MANIFEST describing an image in a registry

# or:
docker buildx imagetools inspect myapp:1.0

# You should see something like:
Name:      myapp:1.0
MediaType: application/vnd.oci.image.manifest.v1+json

# or:
MediaType: application/vnd.docker.distribution.manifest.v2+json


### The registry can contain a manifest like:
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "config": { ... },
  "layers": [ ... ]
}

# The dot notation:
application/vnd.oci.image.manifest.v1+json

# is a MIME/media type string identifying what the JSON document is:
application        = application data
vnd                 = vendor-specific
oci                 = Open Container Initiative
image.manifest      = OCI image manifest
v1                  = OCI manifest media-type version
+json               = represented as JSON

# image manifest - what files/config make up this image
# Kubernetes manifest  - what should Kubernetes create/run

```