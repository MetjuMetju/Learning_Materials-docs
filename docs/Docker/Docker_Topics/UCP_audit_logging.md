### Universal Control Plane overview (UCP) audit logging

- UCP is the older Docker Enterprise product name.
- Modern documentation calls the platform MKE (Mirantis Kubernetes Engine).

### Official docu
https://docs.mirantis.com/containers/v2.1/dockeree-products/ucp.html

- Docker logs and UCP audit logs are different layers serving different purposes.
- UCP audit logging records information about the interaction with the UCP API.
- Docker container logs primarily collecting stdout/stderr produced by the process inside that container.

- Docker container logs              = Container stdout/stderr output.
- UCP audit logs                     = Records of requests/actions made through the UCP API.
- Universal Control Plane (UCP)      = Enterprise cluster management and orchestration platform.

### Other areas names:
- Docker Enterprise                  = Enterprise container platform.
- Docker Engine - Enterprise         = Enterprise container runtime for running containers.
- Docker Trusted Registry (DTR)      = Enterprise private registry for storing container images.

- UCP = Enterprise / commercial product
- Free trial = YES, Free production UCP = NO

### NEW MIRANTIS NAMES

- 1. Mirantis Container Runtime (MCR)
- 2. Mirantis Secure Registry (MSR)
- 3. Mirantis Kubernetes Engine (MKE)

### OLD DOCKER ENTERPRISE NAMES

- 1. Docker Engine - Enterprise (Docker EE)
- 2. Docker Trusted Registry (DTR)
- 3. Universal Control Plane (UCP)

### MAPPING

- 1. Docker EE -> MCR
- 2. DTR -> MSR
- 3. UCP -> MKE

### Installing UCP/MKE

```code
# For example, the official MKE documentation shows:
docker image pull mirantis/ucp:3.7.25

# Then:
docker container run --rm -it \
  --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  mirantis/ucp:3.7.25 install \
  --host-address <node-ip-address> \
  --interactive

# For current MKE 3.x documentation, the general form is:
docker container run --rm -it \
  --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  mirantis/ucp:3.x.y \
  install <command-options>
```

### Check commands:

```code
1. Check whether UCP/MKE is running

docker ps
docker ps --filter name=ucp-controller

### 2. Check the UCP audit logs
docker logs ucp-controller

# For the latest entries:
docker logs ucp-controller --tail 100

# Follow the logs live:
docker logs -f ucp-controller


### 3. Look specifically for audit entries
docker logs ucp-controller 2>&1 | grep '"audit"'

# You can also look for the audit level:
docker logs ucp-controller 2>&1 | grep '"level":"metadata"'

# or:
docker logs ucp-controller 2>&1 | grep '"level":"request"'

### 4. Configure audit logging through the UCP API

# The official documentation shows the API configuration using PUT:
cat > auditlog.json <<'EOF'
{
  "logLevel": "INFO",
  "auditLevel": "metadata",
  "supportDumpIncludeAuditLogs": false
}
EOF

# Then:

curl \
  --cert ${DOCKER_CERT_PATH}/cert.pem \
  --key ${DOCKER_CERT_PATH}/key.pem \
  --cacert ${DOCKER_CERT_PATH}/ca.pem \
  -k \
  -H "Content-Type: application/json" \
  -X PUT \
  --data "$(cat auditlog.json)" \
  https://ucp-domain/api/ucp/config/logging

# The important exam point is:
auditLevel = metadata

# or:
auditLevel = request


### 5. Configure it in the UCP/MKE configuration file

# The configuration section is:

[audit_log_configuration]
level = "metadata"
support_dump_include_audit_logs = false

# Or:

[audit_log_configuration]
level = "request"
support_dump_include_audit_logs = false

# The official documentation says the supported values for level are:
""
"metadata"
"request"

```