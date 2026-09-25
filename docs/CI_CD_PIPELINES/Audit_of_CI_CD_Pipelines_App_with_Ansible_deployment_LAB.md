
https://github.com/MetjuMetju/IstroSec

### Audit cmds (advocacy):

### CLEAN REBUILD FROM SCRATCH

```code

### docker compose down DOES stop the Compose containers first and then removes them.
### Do the Compose cleanup BEFORE deleting the local repository.
### Otherwise the Compose files are gone and Compose cannot use them to identify the project resources.
### The prune commands do NOT stop or remove containers that are currently running.

### 1. STOP DEV CONTAINERS ONLY
docker compose -f docker-compose.dev.yml stop

### 2. REMOVE DEV COMPOSE RESOURCES
docker compose -f docker-compose.dev.yml down --volumes --remove-orphans

### 3. STOP PROD CONTAINERS ONLY
docker compose -f docker-compose.prod.yml stop

### 4. REMOVE PROD COMPOSE RESOURCES
docker compose -f docker-compose.prod.yml down --volumes --remove-orphans

### 5. STOP ANY REMAINING ISTROSEC CONTAINERS
docker ps --filter "name=istrosec"
docker stop $(docker ps -q --filter "name=istrosec") 2>/dev/null || true

### 6. REMOVE ANY REMAINING ISTROSEC CONTAINERS
docker rm -f $(docker ps -aq --filter "name=istrosec") 2>/dev/null || true

### 7. REMOVE ISTROSEC IMAGES
docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}' \
  | grep -E 'istrosec|istrosec-' \
  | awk '{print $2}' \
  | sort -u \
  | xargs -r docker rmi -f

### 8. REMOVE ISTROSEC VOLUMES
docker volume ls --format '{{.Name}}' \
  | grep -E 'istrosec|istrosec-' \
  | xargs -r docker volume rm -f

### 9. REMOVE ISTROSEC NETWORKS
docker network ls --format '{{.Name}}' \
  | grep -E 'istrosec|istrosec-' \
  | xargs -r docker network rm


### 10. REMOVE AND CHECK UNUSED OBJECT
docker container prune -f # REMOVE UNUSED CONTAINERS
docker image prune -f # REMOVE UNUSED IMAGES
docker volume prune -f # REMOVE UNUSED VOLUMES
docker network prune -f # REMOVE UNUSED NETWORKS
docker ps # VERIFY DOCKER CONTAINERS
docker ps -a # VERIFY ALL DOCKER CONTAINERS
docker images # VERIFY DOCKER IMAGES
docker volume ls # VERIFY DOCKER VOLUMES
docker network ls # VERIFY DOCKER NETWORKS

### 11. REMOVE LOCAL TLS CERTIFICATES
rm -rf certs

### 12. REMOVE PYTHON ENVIRONMENT
rm -rf .venv

### 13. REMOVE PYTHON CACHES
rm -rf __pycache__
rm -rf .pytest_cache
rm -rf .ruff_cache

find . -type d -name __pycache__ -prune -exec rm -rf {} +
find . -type d -name .pytest_cache -prune -exec rm -rf {} +
find . -type d -name .ruff_cache -prune -exec rm -rf {} +


### 14. REMOVE LOCAL REPOSITORY
cd ..
rm -rf IstroSec

### 15. VERIFY REPOSITORY IS GONE
ls -la

### OPTIONAL: 16. CLONE CLEAN COPY
git clone https://github.com/MetjuMetju/IstroSec.git
cd IstroSec

### 24. VERIFY GIT STATE
git status
git branch --show-current
git log --oneline -5

### 25. VERIFY PROJECT FILES
git ls-files | sort

find . -maxdepth 3 -type f \
  -not -path './.git/*' \
  | sort
```



### 1. CLONE THE REPOSITORY

cd ~

git clone https://github.com/MetjuMetju/IstroSec.git

cd IstroSec


### 2. CHECK REPOSITORY STATE

git status

git branch --show-current

git remote -v

git log --oneline --decorate -10


### 3. PULL THE LATEST CHANGES

git pull --ff-only


### 4. SHOW ALL TRACKED FILES

git ls-files


### 5. SHOW COMPLETE DIRECTORY STRUCTURE

find . -type f \
  -not -path './.git/*' \
  | sort


### 6. SHOW FILES WITH SIZES

find . -type f \
  -not -path './.git/*' \
  -printf '%s %p\n' \
  | sort -n


### 7. SHOW ALL RELEVANT TEXT FILE CONTENTS

find . -type f \
  -not -path './.git/*' \
  -not -path './.venv/*' \
  -not -path './__pycache__/*' \
  -not -path './.pytest_cache/*' \
  -not -path './.ruff_cache/*' \
  -not -path './certs/*' \
  -not -path './.git/*' \
  | sort \
  | while read -r file; do
      echo
      echo "============================================================"
      echo "FILE: $file"
      echo "============================================================"
      file "$file"
      case "$(file -b --mime "$file")" in
        text/*|application/json*|application/yaml*|application/x-yaml*)
          cat "$file"
          ;;
        *)
          echo "[NON-TEXT FILE - CONTENT NOT PRINTED]"
          ;;
      esac
    done


### 8. INSPECT GITHUB ACTIONS

find .github -type f -print -exec sh -c '
  echo
  echo "============================================================"
  echo "FILE: $1"
  echo "============================================================"
  cat "$1"
' _ {} \;


### 9. INSPECT DOCKER FILES

echo "===== Dockerfile ====="
cat Dockerfile

echo
echo "===== Compose files ====="

for file in docker-compose*.yml compose*.yml compose*.yaml; do
  if [ -f "$file" ]; then
    echo
    echo "============================================================"
    echo "FILE: $file"
    echo "============================================================"
    cat "$file"
  fi
done


### 10. INSPECT PYTHON PROJECT CONFIGURATION

for file in pyproject.toml requirements.txt requirements-dev.txt \
            uv.lock package.json; do
  if [ -f "$file" ]; then
    echo
    echo "============================================================"
    echo "FILE: $file"
    echo "============================================================"
    cat "$file"
  fi
done


### 11. INSPECT NIX / DIRENV

for file in flake.nix flake.lock .envrc; do
  if [ -f "$file" ]; then
    echo
    echo "============================================================"
    echo "FILE: $file"
    echo "============================================================"
    cat "$file"
  fi
done


### 12. INSPECT ANSIBLE STRUCTURE

if [ -d Ansible ]; then
  find Ansible -type f \
    -not -name '*.vault' \
    -not -name '*secret*' \
    | sort
fi


### 13. INSPECT ANSIBLE FILES

if [ -d Ansible ]; then
  find Ansible -type f \
    -not -name '*.vault' \
    -not -name '*secret*' \
    | sort \
    | while read -r file; do
      echo
      echo "============================================================"
      echo "FILE: $file"
      echo "============================================================"
      cat "$file"
    done
fi


### 14. DO NOT PRINT SECRETS

DO NOT run:

cat .env
cat .env.*
cat *vault*
cat *secret*

Do NOT paste:

private keys
passwords
tokens
GitHub credentials
Ansible Vault passwords
API keys


### 15. FIND SECRET-LIKE FILES

find . -type f \
  -not -path './.git/*' \
  \( -name '*.key' \
     -o -name '*.pem' \
     -o -name '*.p12' \
     -o -name '*.pfx' \
     -o -name '*.vault' \
     -o -name '.env' \
     -o -name '.env.*' \) \
  -print


### 16. CHECK GITIGNORE

echo "===== .gitignore ====="
cat .gitignore


### 17. CHECK FOR DOCKER SOCKET USAGE

grep -RIn \
  --exclude-dir=.git \
  --exclude-dir=.venv \
  --exclude='*.lock' \
  'docker.sock\|/var/run/docker' \
  .


### 18. CHECK FOR DOCKER IMAGE BUILDING

grep -RIn \
  --exclude-dir=.git \
  'docker build\|docker/build-push-action\|buildah\|podman build' \
  .github Dockerfile docker-compose*.yml compose*.yml 2>/dev/null


### 19. CHECK TRIVY

grep -RIn \
  --exclude-dir=.git \
  'trivy' \
  .github 2>/dev/null


### 20. CHECK GHCR

grep -RIn \
  --exclude-dir=.git \
  'ghcr.io\|GITHUB_TOKEN\|docker/login-action' \
  .github 2>/dev/null


### 21. CHECK KUBERNETES

find . -type f \
  -not -path './.git/*' \
  \( -name '*.yaml' -o -name '*.yml' \) \
  -print \
  | while read -r file; do
      if grep -qiE 'kind:|apiVersion:|kubectl|kubernetes' "$file"; then
        echo "KUBERNETES FILE: $file"
        cat "$file"
      fi
    done


### 22. CHECK ALL REFERENCES TO THE MAIN TOOLS

grep -RIn \
  --exclude-dir=.git \
  --exclude-dir=.venv \
  -E 'buildah|podman|docker|trivy|ghcr|github actions|pytest|ruff|ansible|flake.nix|direnv|kubernetes|kubectl' \
  . \
  2>/dev/null


### 23. FINAL GIT FILE LIST

git ls-files | sort


### 24. FINAL STATUS

git status --short

git status
