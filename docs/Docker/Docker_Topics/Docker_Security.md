### 10. Docker security

Docker daemon configuration:
- /etc/docker/daemon.json
- system-wide Docker daemon configuration
- check with: docker info

Rootless Docker:
- Docker daemon runs as the unprivileged user
- reduces the impact of a compromised daemon/container
- setup: dockerd-rootless-setuptool.sh install
- check: docker info
- look for: rootless

Daemonless alternatives:
- Podman - daemonless container engine
- Buildah - daemonless image building
- Kubernetes can use containerd or CRI-O instead of Docker Engine

Important distinction:
- Rootless Docker - still Docker, but daemon runs without root privileges
- Podman - no central Docker daemon
- Buildah - builds images, not a full Docker replacement

Useful checks:
- docker info
- systemctl status docker
- cat /etc/docker/daemon.json
- docker context ls
- podman info


### ROOTLESS DOCKER SETUP

1. Check current Docker

docker info
systemctl status docker

2. Install prerequisites

Debian / Ubuntu:

sudo apt update
sudo apt install -y uidmap

3. Check subordinate UID/GID ranges

grep "^$USER:" /etc/subuid
grep "^$USER:" /etc/subgid

You need at least 65536 IDs.

Example:

mates:100000:65536

If missing:

echo "$USER:100000:65536" | sudo tee -a /etc/subuid
echo "$USER:100000:65536" | sudo tee -a /etc/subgid

4. Stop the normal rootful Docker daemon

sudo systemctl disable --now docker.service docker.socket

5. Remove the old socket if necessary

sudo rm -f /var/run/docker.sock

6. Install Rootless Docker

dockerd-rootless-setuptool.sh install

7. Start the user Docker daemon

systemctl --user start docker

8. Enable it automatically

systemctl --user enable docker
sudo loginctl enable-linger $USER

9. Select the rootless Docker context

docker context use rootless

### 10. Check it

```code
docker info

# Look for:
Context: rootless
Security Options: rootless
```

### Why avoid a Docker daemon:
- dockerd is a privileged central process
- Docker daemon compromise can mean host-level compromise
- containers normally depend on the daemon
- daemonless tools reduce this central privileged component

Daemonless alternatives:
- Podman - runs containers without a central Docker daemon
- Buildah - builds container images without a Docker daemon
- BuildKit/buildctl - builds images without dockerd

Rootless Docker:
- still uses dockerd
- daemon runs as non-root user
- reduces privilege
- does NOT make Docker daemonless

Docker
- dockerd
- traditionally root
- rootless mode available

BuildKit
- buildkitd
- can run rootless
- no dockerd

Buildah
- no daemon
- can build rootless
- good for image building

Podman
- no central daemon
- can run rootless
- good for running containers

Best practical rootless combination:
- Buildah - build
- Podman - run
- no Docker daemon

### access to the Docker socket is extremely powerful
```code
docker -H unix:///var/run/docker.sock ps
docker run --rm -it \
  -v /:/host \
  alpine \
  sh
# Inside that container:
chroot /host

# solution:
ls -l /var/run/docker.sock
getent group docker
# remove users from docker
sudo gpasswd -d <user> docker
/home/mates/scripts/chess/BuildKit
id
getent group docker

# The CI job does the image build:
# build-image:
image: quay.io/buildah/stable
script:
- buildah bud -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA" .
- buildah login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" "$CI_REGISTRY"
- buildah push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"

### For security:
- no /var/run/docker.sock
- no docker group
- no privileged Docker daemon
- no permanent Docker daemon inside the CI job
```

# For a new company start with:
Docker image security
- build image
- tag image
- push image
- image signing
- vulnerability scanning
- content trust

GitLab
- source control
- CI/CD
- registry
- vulnerability scanning
- access control

Kubernetes
- isolated execution environment for CI jobs
- RBAC
- Pod Security Admission
- network policies
- ephemeral Pods

Buildah
- image building
- daemonless
- rootless

GitLab Container Scanning
- vulnerability scanning
- Trivy-based
- one primary image scanner

GitLab Registry
- private image storage
- no separate Harbor installation initially

The security improvement is primarily access control and architecture.
containerd itself still has a privileged Unix socket
Access to that socket is also highly privileged.
Kubernetes doesn't normally expose a Docker-style /var/run/docker.sock to users.
Kubernetes uses the CRI (Container Runtime Interface) to communicate with a runtime.
Docker Engine did not natively implement CRI.
So Kubernetes introduced dockershim as an adapter. Kubernetes removed dockershim in v1.24.
But containerd is also a daemon.
Kubernetes did not remove daemons; it moved toward a runtime architecture that fits Kubernetes' CRI model.

Modern setup
- kubelet
- CRI
- containerd OR CRI-O
- runc
The key is interface, not "daemon vs no daemon":
Kubelet - CRI
containerd
runc
container

### Buildah with Podman

echo '<h1>Hello from nginx</h1>' > index.html
buildah bud -t mynginx:1.0 .
buildah from --name mynginx-container mynginx:1.0
buildah inspect mynginx-container

buildah
- reads Dockerfile
- pulls nginx:alpine
- creates filesystem layers
- copies index.html
- creates image
- stores image in local container storage
- exits

podman stop mynginx
podman rm mynginx
podman run -d --name mynginx -p 8080:80 localhost/mynginx:1.0
podman info --format '{{.Host.Security.Rootless}}'
ps aux | grep '[p]odman'
ps -eo user,pid,cmd | grep '[n]ginx'

### BuildKit example - nginx
```code

cd ~/BuildKit
curl -LO https://github.com/moby/buildkit/releases/download/v0.26.2/buildkit-v0.26.2.linux-amd64.tar.gz
tar -xzf buildkit-v0.26.2.linux-amd64.tar.gz
sudo cp bin/buildkitd bin/buildctl /usr/local/bin/

which buildkitd
which rootlesskit
buildkitd --version
buildctl --version
ps aux | grep '[b]uildkitd'
ps aux | grep '[r]ootlesskit'
ss -lx | grep buildkit

mkdir -p ~/bin
cd ~/bin
# after downloading the BuildKit Linux amd64 release:
tar -xzf buildkit-v*.linux-amd64.tar.gz
export PATH="$HOME/bin:$PATH"

Dockerfile:
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html

# Start BuildKit daemonless/rootless:
rootlesskit buildkitd &

# Build the image:
buildctl build \
  --frontend=dockerfile.v0 \
  --local context=. \
  --local dockerfile=. \
  --output type=image,name=localhost:5000/mynginx:1.0

```