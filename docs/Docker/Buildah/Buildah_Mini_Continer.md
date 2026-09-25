### Minimal Docker File:

vi Dockerfile

```code

FROM registry.access.redhat.com/ubi9/ubi-micro
# Minimal shell package
RUN microdnf install -y bash && microdnf clean all
# Create unprivileged user
USER 1001
WORKDIR /home/shell
# Restricted bash
ENTRYPOINT ["/bin/bash", "--restricted"]
```

### Buil With Buildah on Red Hat

buildah bud -t restricted-shell:latest .
#### or:
podman build -t restricted-shell .
#### Containerfile + buildah bud - Buildah commits automatically

# Or with script and without Docker file:

```code
vi build_container.sh
#!/bin/bash
container=$(buildah from registry.access.redhat.com/ubi9/ubi-micro)
buildah run "$container" -- microdnf install -y bash
buildah run "$container" -- microdnf clean all
buildah config \
  --user 1001 \
  --workingdir /home/shell \
  --entrypoint '["/bin/bash","--restricted"]' \
  "$container"
buildah commit "$container" restricted-shell:latest

```

### Or build with Podman:
### Run interactively:
podman run --rm -it \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --network=none \
  --user=1001 \
  restricted-shell

bash --restricted alone is not a security boundary. For exposing this to users, I recommend combining:

--read-only
--cap-drop=ALL
--security-opt=no-new-privileges
--network=none (unless networking is needed)
non-root user
no host mounts
CPU/memory/PID limits
SELinux enforcing on Red Hat
ideally seccomp/AppArmor-equivalent controls where applicable


### a whitelist of allowed commands only
### SSH or web-terminal exposure without giving users container escape opportunities.
