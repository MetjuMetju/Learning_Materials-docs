
https://github.com/MetjuMetju/IstroSec


### CURRENT STATUS

### 1. APPLICATION

  - The application is a minimal HTTPS web application.

#### The repository contains:

    app/
    tests/
    VERSION

#### The Dockerfile currently uses:

    Python 3.12
    Flask
    Gunicorn

- It has separate targets for:

    - development
    - production

  - This satisfies the multi-stage build requirement
  - The Dockerfile has base, dependencies, development and production stages


### 2. APPLICATION VERSIONING

- It has file named:

    VERSION

- The version is included in the Docker image/application


### 3. DOCKER MULTI-STAGE BUILD

Dockerfile contains:

    FROM python:3.12-slim AS base
    FROM base AS dependencies
    FROM base AS development
    FROM base AS production


### 4. DOCKER COMPOSE

The repository has:

    docker-compose.dev.yml
    docker-compose.prod.yml

- Both contain a TLS bootstrap service

Both generate/use:

    server.crt
    server.key

- The repository uses ONE certificate volume, not two separate certificate sets.

The current Compose implementation uses a named Docker volume:

    certs

### 5. TLS / HTTPS

- The application uses a self-signed X.509 certificate.
- The certificate is generated during deployment.
- The repository README explicitly states that the lab uses a self-signed certificate.
- The Dockerfile configures HTTPS for both development and production.
- Development uses Flask's HTTPS support.

Production uses Gunicorn with:

    --certfile
    --keyfile

### 6. CODE QUALITY

- The repository uses: Ruff

The GitHub Actions quality workflow performs:

    ruff format --check .
    ruff check .

- It also runs pytest


### 7. APPLICATION TESTS

The repository contains:

    tests/test_main.py

The GitHub quality workflow runs:

    pytest


### 8. GITHUB ACTIONS

The repository has:

    .github/workflows/

With:

    docker.yml
    quality.yml
    security.yml


### 9. GHCR

docker.yml publishes the image to:

    ghcr.io/metjumetju/istrosec

The workflow authenticates to GHCR using:

    GITHUB_TOKEN

- The workflow currently builds and pushes the production image.


### 10. TRIVY

security.yml uses:

    aquasec/trivy:0.73.0

- It scans the production Docker image.
- It fails the workflow for: CRITICAL - vulnerabilities that are not fixed are ignored (the security gate exists)

### 11. GitHub workflow

GitHub workflow uses:

    docker/build-push-action

and:

    docker build


### 12. DOCKER SOCKET

The current Trivy workflow runs:

    docker run

and mounts:

    /var/run/docker.sock


### 13. ANSIBLE

The repository now contains a substantial Ansible deployment layer:
```code
  Ansible/
      inventories/
          dev/
          prod/
      roles/
          docker_app/
      playbooks/
          install-docker.yml
          deploy.yml
          update.yml
```

There are also:

    DEV inventory
    PROD inventory
    Vault files
    separate Vault IDs


### 14. CI/CD

CI is clearly present:

    quality
    tests
    image build
    GHCR push
    security scan

- Deployment/CD is also present through Ansible
- The current deployment target is Docker hosts managed by Ansible

### 15. FLAKE.NIX

The repository contains:

    flake.nix

It provides tools including:

    Python
    uv
    Docker
    Docker Compose
    Git
    OpenSSL
    direnv

The repository also contains:

    .envrc

### 16. README

README.md exists and documents:

    application
    CI
    GHCR
    Ansible
    DEV/PROD environments
    TLS
    deployment
    repository structure


### FINAL STATUS

DONE:

    Application
    Versioning
    Multi-stage Dockerfile
    Development target
    Production target
    Docker Compose
    TLS bootstrap
    Self-signed HTTPS
    Code quality
    Tests
    GitHub Actions
    GHCR
    Trivy
    Ansible deployment
    flake.nix
    direnv
    README

NEEDS CORRECTION:

    Rootless Buildah
    Remove Docker-based image building from CI
    Remove docker.sock dependency from security scanning

NOT DONE:

    Kubernetes final phase
