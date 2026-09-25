
https://github.com/MetjuMetju/IstroSec

### Audit cmds (advocacy):

```code
sudo docker network ls
NETWORK ID     NAME                          DRIVER    SCOPE
34cf0c2facf5   bridge                        bridge    local
c4a9ccb1a47f   host                          host      local
2e08e3968d6f   istrosec-dev-app01_default    bridge    local
5efe4dcd848d   istrosec-dev-app02_default    bridge    local
d64457a4153e   istrosec-prod-app01_default   bridge    local
9a1946f73a2a   istrosec-prod-app02_default   bridge    local
53a18904ac7d   kind                          bridge    local
74a6182a0629   none                          null      local

sudo docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED       STATUS      PORTS                                         NAMES
1644a9f0c80c   kindest/node:v1.37.0               "/usr/local/bin/entr…"   5 days ago    Up 4 days   127.0.0.1:38001->6443/tcp                     kind-control-plane
6029a020bc08   ghcr.io/metjumetju/istrosec:main   "gunicorn --bind 0.0…"   2 weeks ago   Up 5 days   0.0.0.0:5005->5000/tcp, [::]:5005->5000/tcp   istrosec-prod-app02
e8b8dc8be301   ghcr.io/metjumetju/istrosec:main   "gunicorn --bind 0.0…"   2 weeks ago   Up 5 days   0.0.0.0:5004->5000/tcp, [::]:5004->5000/tcp   istrosec-prod-app01
5eac854b1cf1   ghcr.io/metjumetju/istrosec:main   "gunicorn --bind 0.0…"   2 weeks ago   Up 5 days   0.0.0.0:5002->5000/tcp, [::]:5002->5000/tcp   istrosec-dev-app01
4b58e41eb3db   ghcr.io/metjumetju/istrosec:main   "gunicorn --bind 0.0…"   2 weeks ago   Up 5 days   0.0.0.0:5003->5000/tcp, [::]:5003->5000/tcp   istrosec-dev-app02


cat /opt/istrosec-dev-app01/docker-compose.yml
services:
  bootstrap:
    image: alpine:3.22
    volumes:
      - certs:/certs
    command:
      - /bin/sh
      - -c
      - |
        apk add --no-cache openssl
        if [ ! -f /certs/server.crt ] || [ ! -f /certs/server.key ]; then
          openssl req -x509 -newkey rsa:2048 -nodes \
            -keyout /certs/server.key \
            -out /certs/server.crt \
            -days 365 \
            -subj "/CN=localhost"
        fi
        chown 10001:10001 /certs/server.crt /certs/server.key
        chmod 644 /certs/server.crt
        chmod 600 /certs/server.key
  istrosec:
    image: ghcr.io/metjumetju/istrosec:main
    container_name: istrosec-dev-app01
    restart: unless-stopped
    ports:
      - "5002:5000"
    environment:
      APP_ENV: "development"
    volumes:
      - certs:/certs:ro
    depends_on:
      bootstrap:
        condition: service_completed_successfully
    pull_policy: always
volumes:
  certs:



sudo cat /opt/istrosec-prod-app01/docker-compose.yml
services:
  bootstrap:
    image: alpine:3.22
    volumes:
      - certs:/certs
    command:
      - /bin/sh
      - -c
      - |
        apk add --no-cache openssl
        if [ ! -f /certs/server.crt ] || [ ! -f /certs/server.key ]; then
          openssl req -x509 -newkey rsa:2048 -nodes \
            -keyout /certs/server.key \
            -out /certs/server.crt \
            -days 365 \
            -subj "/CN=localhost"
        fi
        chown 10001:10001 /certs/server.crt /certs/server.key
        chmod 644 /certs/server.crt
        chmod 600 /certs/server.key
  istrosec:
    image: ghcr.io/metjumetju/istrosec:main
    container_name: istrosec-prod-app01
    restart: unless-stopped
    ports:
      - "5004:5000"
    environment:
      APP_ENV: "production"
    volumes:
      - certs:/certs:ro
    depends_on:
      bootstrap:
        condition: service_completed_successfully
    pull_policy: always
volumes:
  certs:


# 1. STOP ISTROSEC CONTAINERS
sudo docker stop istrosec-dev-app01 istrosec-dev-app02 istrosec-prod-app01 istrosec-prod-app02

# 2. REMOVE ISTROSEC CONTAINERS
sudo docker rm istrosec-dev-app01 istrosec-dev-app02 istrosec-prod-app01 istrosec-prod-app02

# 3. REMOVE ISTROSEC DEPLOYMENT DIRECTORIES
sudo rm -rf /opt/istrosec-dev-app01
sudo rm -rf /opt/istrosec-prod-app01

# 4. REMOVE ISTROSEC VOLUMES
sudo docker volume ls --format '{{.Name}}' | grep 'istrosec' | xargs -r sudo docker volume rm

# 5. VERIFY ISTROSEC CONTAINERS ARE GONE
sudo docker ps -a --filter "name=istrosec"


.github/workflows/quality.yml
.github/workflows/docker.yml
.github/workflows/security.yml


BASED ONLY ON THE PROJECT YOU JUST PULLED:

There is NO Kubernetes / K8s in the repository.

The actual top-level project areas are:

1. app/
   Application

2. tests/
   Tests

3. Dockerfile
   Multi-stage Docker build

4. docker-compose.dev.yml
   Local development + TLS bootstrap

5. docker-compose.prod.yml
   Local production + TLS bootstrap

6. .github/workflows/
   GitHub Actions CI/CD

7. Ansible/
   Deployment / configuration management

8. flake.nix
   Development environment

9. requirements.txt
   Production dependencies

10. requirements-dev.txt
    Development dependencies

11. VERSION
    Application versioning

12. README.md
    Documentation

THAT IS WHAT EXISTS IN THE PULLED REPOSITORY.

KUBERNETES IS NOT PART OF THIS CURRENT REPOSITORY STRUCTURE.

So for the audit, we should NOT put Kubernetes into the repository areas.

NEXT INSPECTION SHOULD BE:

1. app/
2. tests/
3. Dockerfile
4. docker-compose.dev.yml
5. docker-compose.prod.yml
6. .github/workflows/
7. Ansible/
8. flake.nix
9. VERSION
10. README.md

```




### DETAILED EXPLANATION OF THE CURRENT ISTROSEC ENVIRONMENT

```code

sudo docker ps

### Your current docker-compose.dev.yml says:
5001:5000
### Your current docker-compose.prod.yml says:
5002:5000

### ISTROSEC PRODUCTION CONTAINER

# CONTAINER:
istrosec-prod-app01
# IMAGE:
ghcr.io/metjumetju/istrosec:main



https://localhost:5004
# goes to:
istrosec-prod-app01:5000



# Both containers use the image:
ghcr.io/metjumetju/istrosec:main

# They are running an image pulled from GitHub Container Registry
# rather than an image that Docker Compose necessarily built locally at startup.

### ISTROSEC DEVELOPMENT CONTAINERS

# These are two running IstroSec development application instances.
# CONTAINER:
istrosec-dev-app01
# PORT:
5002 -> 5000

# CONTAINER:
istrosec-dev-app02
# PORT:
5003 -> 5000


BUT docker ps shows:

dev-app01  = 5002:5000
dev-app02  = 5003:5000
prod-app01 = 5004:5000
prod-app02 = 5005:5000

Your repository contains:

Ansible/

and the README indicates that Ansible is used for deployment.

So the running containers with names:

istrosec-dev-app01
istrosec-dev-app02
istrosec-prod-app01
istrosec-prod-app02

are consistent with your Ansible-based multi-host deployment.

This is important when debugging Docker Compose.


============================================================
6. docker-compose.dev.yml
============================================================

The development Compose file defines two services:

bootstrap
app


============================================================
7. BOOTSTRAP SERVICE
============================================================

SERVICE:

bootstrap

IMAGE:

alpine:3.22

PURPOSE:

The bootstrap container prepares the TLS certificate files before the
application starts.

It mounts:

certs:/certs

This means Docker provides a named volume called:

certs

inside the Compose project.

The container then installs:

openssl

using:

apk add --no-cache openssl


============================================================
8. TLS CERTIFICATE GENERATION
============================================================

The bootstrap script checks:

if [ ! -f /certs/server.crt ] || [ ! -f /certs/server.key ]

Meaning:

IF the certificate OR private key does not exist,

THEN generate them.

The command:

openssl req -x509 -newkey rsa:2048 -nodes

creates a self-signed X.509 certificate and RSA private key.

The files are:

/certs/server.crt
/certs/server.key


The certificate is valid for:

365 days


The certificate subject is:

CN=localhost


This is appropriate for a local laboratory environment.

It is NOT equivalent to a publicly trusted production certificate.


============================================================
9. DEVELOPMENT TLS PERMISSIONS
============================================================

The development bootstrap runs:

chmod 644 /certs/server.crt

The certificate can therefore be read by normal processes.

Then:

chmod 600 /certs/server.key

The private key is restricted more strongly.

This is correct because the private key is sensitive and should not
be world-readable.


============================================================
10. DEVELOPMENT APPLICATION
============================================================

The app service uses:

build:
  context: .
  target: development

This tells Docker:

Build the Dockerfile from the current directory.

But do NOT use the final production stage.

Instead use:

development


============================================================
11. DEVELOPMENT TARGET
============================================================

Your Dockerfile contains:

FROM base AS development

This stage installs:

requirements.txt

and:

requirements-dev.txt

Therefore the development image contains both application and
development dependencies.

It also copies:

app
tests
VERSION


The application runs using Flask:

flask --app app.main:app run


and listens on:

0.0.0.0:5000


HTTPS is enabled with:

--cert=/certs/server.crt
--key=/certs/server.key


============================================================
12. DEVELOPMENT VOLUMES
============================================================

The development application mounts:

.:/app

This means your local repository directory is mounted into:

/app

inside the container.

This is useful for development because source-code changes on the
host can immediately be visible inside the container.

It also mounts:

certs:/certs:ro

The:

ro

means:

READ ONLY

The application can read the certificates but cannot modify them.


============================================================
13. depends_on
============================================================

The app contains:

depends_on:
  bootstrap:
    condition: service_completed_successfully

This is important.

It tells Compose:

Do not start the application until the bootstrap service has completed
successfully.

Therefore the intended sequence is:

bootstrap generates/prepares TLS files

then:

app starts

This prevents the application from starting before its certificate
and private key exist.


============================================================
14. PRODUCTION COMPOSE
============================================================

docker-compose.prod.yml uses the same general architecture:

bootstrap
app


The important difference is:

target: production


instead of:

target: development


============================================================
15. PRODUCTION BOOTSTRAP
============================================================

The production bootstrap also generates:

server.crt
server.key

if they do not already exist.

Then it runs:

chown 10001:10001 /certs/server.crt /certs/server.key


This is important because the production Dockerfile creates:

appuser

with UID:

10001


Therefore the application user can access the TLS files.


============================================================
16. PRODUCTION SECURITY
============================================================

The production Dockerfile contains:

RUN useradd --create-home --uid 10001 --shell /bin/bash appuser

Then:

USER appuser

Therefore Gunicorn does NOT run as root.

This is an important container-security practice.

The production container runs the application as:

UID 10001

instead of:

root


============================================================
17. PRODUCTION DOCKERFILE
============================================================

Your Dockerfile has multiple stages:

base
dependencies
development
production


This is your:

MULTI-STAGE BUILD


============================================================
18. BASE STAGE
============================================================

FROM python:3.12-slim AS base

This establishes the common Python environment.

It also sets:

WORKDIR /app

Therefore application files are located under:

/app


============================================================
19. DEPENDENCIES STAGE
============================================================

FROM base AS dependencies

This stage installs only:

requirements.txt

into:

/opt/venv


The virtual environment is later copied into the production image.

This allows the production image to reuse the prepared Python
environment without needing to install the dependencies again.


============================================================
20. DEVELOPMENT STAGE
============================================================

FROM base AS development

Installs:

requirements.txt
requirements-dev.txt

Then copies:

app
tests
VERSION


It runs Flask's development server.

This stage is intended for development and testing.


============================================================
21. PRODUCTION STAGE
============================================================

FROM base AS production

The production stage starts from the clean base image.

It copies:

/opt/venv

from:

dependencies


Then it copies:

app
VERSION


It does NOT copy:

tests


That helps keep the production image smaller and avoids unnecessarily
shipping test code.


============================================================
22. PRODUCTION USER
============================================================

The production image creates:

appuser

UID:

10001

Then:

USER appuser

Therefore the application does not run with root privileges.

This reduces the impact of a possible application/container
compromise.


============================================================
23. GUNICORN
============================================================

Production starts:

gunicorn

instead of Flask's development server.

Gunicorn is a production WSGI server for Python web applications.

Your configuration uses:

--workers 2

Therefore the application starts two Gunicorn worker processes.


============================================================
24. HTTPS IN PRODUCTION
============================================================

Gunicorn is configured with:

--certfile=/certs/server.crt

and:

--keyfile=/certs/server.key


Therefore HTTPS is terminated directly by Gunicorn.

The application itself is listening on:

5000


The TLS connection is established directly with the application
container.


============================================================
25. WHAT YOUR ARCHITECTURE CURRENTLY DOES
============================================================

At a high level:

GitHub
  |
  | application source
  v
GitHub Actions
  |
  | container image
  v
GHCR
  |
  | ghcr.io/metjumetju/istrosec:main
  v
Docker containers
  |
  +-- dev-app01
  +-- dev-app02
  +-- prod-app01
  +-- prod-app02


Separately:

Docker
  |
  +-- KIND
       |
       +-- Kubernetes control plane


============================================================
26. IMPORTANT: YOUR KUBERNETES ENVIRONMENT IS ALREADY RUNNING
============================================================

Your:

kind-control-plane

container proves that you already have a KIND Kubernetes control plane
running inside Docker.

Therefore your environment currently contains BOTH:

IstroSec Docker deployments

AND:

a Kubernetes environment.


============================================================
27. WHY THIS MATTERS FOR CLEANUP
============================================================

If you execute:

docker container prune -f

Docker removes only stopped containers.

Your five containers are:

Up

so they are not removed.

Therefore:

kind-control-plane

will remain running.

And:

istrosec-prod-app01
istrosec-prod-app02
istrosec-dev-app01
istrosec-dev-app02

will remain running.


### YOUR MOST IMPORTANT COMMANDS
docker ps # SHOW ONLY ACTIVE/RUNNING CONTAINERS
docker ps -a # SHOW ACTIVE + INACTIVE/STOPPED CONTAINERS
docker images # SHOW LOCAL DOCKER IMAGES
docker volume ls # SHOW DOCKER VOLUMES
docker network ls # SHOW DOCKER NETWORKS
```
