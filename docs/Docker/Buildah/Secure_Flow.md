Source security — SAST, SCA, secrets
Build — Buildah, trusted/minimal base
Image scanning — CVEs, malware, config
SBOM — software inventory
Provenance — build origin/attestation
Signing — Sigstore/Cosign
Registry security — TLS, RBAC, audit
Encryption — at-rest + optional OCI image encryption
Immutable identity — digest pinning
Admission — signature/policy verification
Runtime security — non-root, SELinux, seccomp, capabilities
Network security — ingress/egress policy
Monitoring — logging, detection
Vulnerability response — rebuild, rotate, revoke/promote

```code
vi Dockerfile
FROM registry.access.redhat.com/ubi9/ubi

RUN dnf install -y \
        bash \
        buildah \
        git \
        make \
        gcc \
        gcc-c++ \
        tar \
        gzip \
        findutils \
        curl-minimal \
    && dnf clean all \
    && rm -rf /var/cache/dnf
RUN useradd -u 1000 -m -s /bin/bash builder
# ttyd
RUN curl -L \
    https://github.com/tsl0922/ttyd/releases/latest/download/ttyd.x86_64 \
    -o /usr/local/bin/ttyd \
    && chmod 755 /usr/local/bin/ttyd
USER builder
WORKDIR /home/builder
EXPOSE 7681
# ENTRYPOINT ["/usr/local/bin/ttyd", "--port", "7681", "/bin/bash", "--restricted"]
ENTRYPOINT ["/usr/local/bin/ttyd", "--writable", "--port", "7681", "/bin/bash", "--restricted"]
```
sudo docker build --no-cache -t restricted-shell .
sudo docker run --rm -p 7681:7681 restricted-shell

http://localhost:7681

sudo docker build -t restricted-shell .
sudo docker images restricted-shell

sudo docker run --rm -it restricted-shell
whoami
buildah --version
