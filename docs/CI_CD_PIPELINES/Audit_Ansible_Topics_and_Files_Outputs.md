### Ansible part:
ls -l Ansible
total 8
-rw-r--r--. 1 mates mates 227 Aug 17 13:49 ansible.cfg
drwxr-xr-x. 4 mates mates  29 Aug 17 14:21 inventories
drwxr-xr-x. 2 mates mates  68 Aug 18 15:39 playbooks
-rw-r--r--. 1 mates mates 229 Aug 17 17:52 requirements.yml
drwxr-xr-x. 4 mates mates  50 Aug 17 17:14 roles


sudo docker inspect istrosec-dev-app01 --format '{{json .Config.Labels}}'

/opt/istrosec-dev-app01/docker-compose.yml


1. ansible.cfg
2. inventories/
3. playbooks/
4. requirements.yml
5. roles/

find Ansible -type f | wc -l
52
find Ansible/inventories -type f | wc -l
10
find Ansible/playbooks -type f | wc -l
3
find Ansible/roles -type f | wc -l
37

find Ansible -type f \( -name "*.yml" -o -name "*.yaml" \) | wc -l
42

find Ansible -type f -print -exec sh -c 'echo; echo "===== $1 ====="; cat "$1"' _ {} \;

1. TOP-LEVEL ANSIBLE FILES
cat Ansible/ansible.cfg
cat Ansible/requirements.yml

2. INVENTORIES
find Ansible/inventories -type f -print
Ansible/inventories/dev/group_vars/all/vault.yml
Ansible/inventories/dev/group_vars/app_servers.yml
Ansible/inventories/dev/host_vars/dev-app01.yml
Ansible/inventories/dev/host_vars/dev-app02.yml
Ansible/inventories/dev/hosts.yml
Ansible/inventories/prod/group_vars/all/vault.yml
Ansible/inventories/prod/group_vars/app_servers.yml
Ansible/inventories/prod/host_vars/prod-app01.yml
Ansible/inventories/prod/host_vars/prod-app02.yml
Ansible/inventories/prod/hosts.yml

3. PLAYBOOKS
find Ansible/playbooks -type f -print
Ansible/playbooks/deploy.yml
Ansible/playbooks/install-docker.yml
Ansible/playbooks/update.yml

4. ROLES
find Ansible/roles -type f -print
Ansible/roles/docker_app/README.md
Ansible/roles/geerlingguy.docker/.ansible-lint
Ansible/roles/geerlingguy.docker/.gitignore
Ansible/roles/geerlingguy.docker/.yamllint
Ansible/roles/geerlingguy.docker/LICENSE
Ansible/roles/geerlingguy.docker/README.md

find Ansible/roles -type f -print
Ansible/roles/docker_app/README.md
Ansible/roles/docker_app/defaults/main.yml
Ansible/roles/docker_app/handlers/main.yml
Ansible/roles/docker_app/meta/main.yml
Ansible/roles/docker_app/tasks/main.yml
Ansible/roles/docker_app/templates/docker-compose.yml.j2
Ansible/roles/docker_app/tests/inventory
Ansible/roles/docker_app/tests/test.yml
Ansible/roles/docker_app/vars/main.yml
Ansible/roles/geerlingguy.docker/.ansible-lint
Ansible/roles/geerlingguy.docker/.github/FUNDING.yml
Ansible/roles/geerlingguy.docker/.github/workflows/ci.yml
Ansible/roles/geerlingguy.docker/.github/workflows/release.yml
Ansible/roles/geerlingguy.docker/.github/workflows/stale.yml
Ansible/roles/geerlingguy.docker/.gitignore
Ansible/roles/geerlingguy.docker/.yamllint
Ansible/roles/geerlingguy.docker/LICENSE
Ansible/roles/geerlingguy.docker/README.md
Ansible/roles/geerlingguy.docker/defaults/main.yml
Ansible/roles/geerlingguy.docker/handlers/main.yml
Ansible/roles/geerlingguy.docker/meta/.galaxy_install_info
Ansible/roles/geerlingguy.docker/meta/main.yml
Ansible/roles/geerlingguy.docker/molecule/default/converge.yml
Ansible/roles/geerlingguy.docker/molecule/default/molecule.yml
Ansible/roles/geerlingguy.docker/molecule/default/verify.yml
Ansible/roles/geerlingguy.docker/tasks/docker-compose.yml
Ansible/roles/geerlingguy.docker/tasks/docker-users.yml
Ansible/roles/geerlingguy.docker/tasks/main.yml
Ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml
Ansible/roles/geerlingguy.docker/tasks/setup-RedHat.yml
Ansible/roles/geerlingguy.docker/tasks/setup-Suse.yml
Ansible/roles/geerlingguy.docker/vars/Alpine.yml
Ansible/roles/geerlingguy.docker/vars/Archlinux.yml
Ansible/roles/geerlingguy.docker/vars/Debian.yml
Ansible/roles/geerlingguy.docker/vars/RedHat.yml
Ansible/roles/geerlingguy.docker/vars/Suse.yml
Ansible/roles/geerlingguy.docker/vars/main.yml




###

1. root folder files:

cat Ansible/ansible.cfg
[defaults]
roles_path = ./roles
host_key_checking = False
retry_files_enabled = False
stdout_callback = default
interpreter_python = auto_silent
[privilege_escalation]
become = True
become_method = sudo
become_ask_pass = False

cat Ansible/requirements.yml
---
roles:
  - name: geerlingguy.docker
    src: https://github.com/geerlingguy/ansible-role-docker.git
    version: "1d3968dbf0df48515ffda0f6561cbd25206f502a"

collections:
  - name: community.docker
  - name: community.general


### 2. INVENTORIES
cat Ansible/inventories/dev/hosts.yml
cat Ansible/inventories/dev/group_vars/app_servers.yml
cat Ansible/inventories/dev/group_vars/all/vault.yml
cat Ansible/inventories/dev/host_vars/dev-app01.yml
cat Ansible/inventories/dev/host_vars/dev-app02.yml


cat Ansible/inventories/dev/hosts.yml
---
all:
  children:
    docker_hosts:
      children:
        app_servers:
          hosts:
            dev-app01:
              ansible_host: 192.168.0.215
              ansible_user: mates
            dev-app02:
              ansible_host: 192.168.0.215
              ansible_user: mates


cat Ansible/inventories/dev/group_vars/app_servers.yml
---
app_name: istrosec
app_environment: development
app_image: ghcr.io/metjumetju/istrosec:main
app_container_port: 5000

cat Ansible/inventories/dev/group_vars/all/vault.yml
```code
$ANSIBLE_VAULT;1.1;AES256
61616662663536383...
```

cat Ansible/inventories/dev/host_vars/dev-app01.yml
---
app_host_port: 5002

cat Ansible/inventories/dev/host_vars/dev-app02.yml
---
app_host_port: 5003


### 3. PRODUCTION INVENTORY
cat Ansible/inventories/prod/hosts.yml
cat Ansible/inventories/prod/group_vars/app_servers.yml
cat Ansible/inventories/prod/group_vars/all/vault.yml
cat Ansible/inventories/prod/host_vars/prod-app01.yml
cat Ansible/inventories/prod/host_vars/prod-app02.yml

cat Ansible/inventories/prod/hosts.yml
prod-app01
    host: 192.168.0.215
    user: mates
    host port: 5004

prod-app02
    host: 192.168.0.215
    user: mates
    host port: 5005

GROUP DEFAULTS FOR BOTH PRODUCTION HOSTS:

app_name: istrosec
app_environment: production
app_image: ghcr.io/metjumetju/istrosec:main
app_container_port: 5000

HOST-SPECIFIC OVERRIDES:

prod-app01:
    app_host_port: 5004

prod-app02:
    app_host_port: 5005

prod-app01:
    APP_ENV=production
    host port 5004
    container port 5000

prod-app02:
    APP_ENV=production
    host port 5005
    container port 5000

prod-app01
    192.168.0.215:5004 -> container:5000
prod-app02
    192.168.0.215:5005 -> container:5000


prod/group_vars/app_servers.yml       # production-wide configuration
prod/host_vars/prod-app01.yml         # host-specific configuration
prod/host_vars/prod-app02.yml         # host-specific configuration

prod-app01 and prod-app02 have the SAME ansible_host:
192.168.0.215



cat Ansible/inventories/prod/hosts.yml
---
all:
  children:
    docker_hosts:
      children:
        app_servers:
          hosts:
            prod-app01:
              ansible_host: 192.168.0.215
              ansible_user: mates
            prod-app02:
              ansible_host: 192.168.0.215
              ansible_user: mates

cat Ansible/inventories/prod/group_vars/app_servers.yml
---
app_name: istrosec
app_environment: production
app_image: ghcr.io/metjumetju/istrosec:main
app_container_port: 5000

cat Ansible/inventories/prod/group_vars/all/vault.yml

```code
cat Ansible/inventories/prod/group_vars/all/vault.yml
$ANSIBLE_VAULT;1.1;AES256
36366...
```

cat Ansible/inventories/prod/host_vars/prod-app01.yml
---
app_host_port: 5004
cat Ansible/inventories/prod/host_vars/prod-app02.yml
---
app_host_port: 5005

### 4. PLAYBOOKS
cat Ansible/playbooks/install-docker.yml
cat Ansible/playbooks/deploy.yml
cat Ansible/playbooks/update.yml


cat Ansible/playbooks/install-docker.yml
---
- name: Install Docker on all Docker hosts
  hosts: docker_hosts
  become: true
  roles:
    - role: geerlingguy.docker

cat Ansible/playbooks/deploy.yml
---
- name: Deploy IstroSec application
  hosts: app_servers
  become: true
  roles:
    - role: docker_app

cat Ansible/playbooks/update.yml
cat Ansible/playbooks/update.yml
---
- name: Update IstroSec application
  hosts: app_servers
  become: true
  tasks:
    - name: Log in to GitHub Container Registry
      community.docker.docker_login:
        registry_url: ghcr.io
        username: "{{ vault_registry_username }}"
        password: "{{ vault_registry_token }}"
        reauthorize: true
      no_log: true
    - name: Pull latest application image
      community.docker.docker_image:
        name: "{{ app_image }}"
        source: pull
    - name: Recreate application with latest image
      community.docker.docker_compose_v2:
        project_src: "{{ app_project_dir }}"
        state: present
        pull: always
        recreate: always

### These 3 playbooks are the main execution layer of the Ansible part.

There are THREE different purposes:

1. install-docker.yml - Install Docker on the target Linux hosts.
2. deploy.yml - Deploy IstroSec for the first time.
3. update.yml - Update an already deployed IstroSec application to the latest image.

1. install-docker.yml

- name: Install Docker on all Docker hosts
  hosts: docker_hosts
  become: true
  roles:
    - role: geerlingguy.docker

roles:
  - name: geerlingguy.docker
    src: https://github.com/geerlingguy/ansible-role-docker.git
    version: "1d3968db..."

The role is not technically required for Ansible itself.
It is a reusable automation package that saves you from writing the
Docker installation logic yourself.

WITHOUT geerlingguy.docker
You would replace:
- name: Install Docker
  hosts: docker_hosts
  become: true
  roles:
    - role: geerlingguy.docker
with your own tasks, for example on Red Hat/Rocky/AlmaLinux:
- name: Install Docker packages
  ansible.builtin.dnf:
    name:
      - docker-ce
      - docker-ce-cli
      - containerd.io
      - docker-buildx-plugin
      - docker-compose-plugin
    state: present
- name: Start Docker
  ansible.builtin.systemd:
    name: docker
    state: started
    enabled: true
- name: Add user to docker group
  ansible.builtin.user:
    name: "{{ ansible_user }}"
    groups: docker
    append: true

##### WHAT IT DOES:
hosts: docker_hosts

This selects the inventory group:
docker_hosts

Your inventory has:
all
  docker_hosts
    app_servers
      prod-app01
      prod-app02

So the Docker installation is applied to all hosts belonging to docker_hosts.

become: true  # Ansible becomes privileged, normally using sudo.
This is required because installing Docker modifies system packages, services, users, repositories, etc.

roles:
  - role: geerlingguy.docker
This delegates the actual Docker installation to the external geerlingguy.docker Ansible role.

You have that role under:
Ansible/roles/geerlingguy.docker/

So this playbook itself contains almost no Docker installation logic.
It says: "Run the geerlingguy.docker role against every docker_hosts host."


2. deploy.yml

- name: Deploy IstroSec application
  hosts: app_servers
  become: true
  roles:
    - role: docker_app


WHAT IT DOES:
hosts: app_servers

Only hosts in the app_servers group are targeted.
prod-app01
prod-app02

become: true
Deployment runs with elevated privileges.

That makes sense because the role creates:
/opt/istrosec-...
and manages Docker/Compose.

roles:
  - role: docker_app

This runs YOUR project-specific role:
Ansible/roles/docker_app/

That role then:
1. Creates the application directory.
2. Logs into GHCR.
3. Generates docker-compose.yml from the Jinja2 template.
4. Starts the Compose application.
5. Pulls the configured image.


install-docker.yml    # prepares the host
deploy.yml            # deploys the application

3. update.yml

It does NOT use the docker_app role. Instead, it directly performs the update tasks.

TASK 1:
community.docker.docker_login

Logs into:
ghcr.io

using:
vault_registry_username
vault_registry_token

The credentials come from Ansible Vault.
no_log: true

prevents the credentials from being printed in Ansible output.

TASK 2:
community.docker.docker_image

name: "{{ app_image }}"
source: pull

This pulls the configured application image.
For production, app_image comes from:
ghcr.io/metjumetju/istrosec:main

TASK 3:
community.docker.docker_compose_v2

project_src: "{{ app_project_dir }}"
state: present
pull: always
recreate: always


The docker_app role already does:
docker_login
docker-compose configuration
docker compose start/update
pull: always

But update.yml separately does:
docker_login
docker_image pull
docker compose recreate

That is not necessarily wrong.

It gives you a dedicated explicit "update" operation.

And it DOES:
update.yml uses:
app_project_dir

and:
app_image

So those variables must come from the inventory/group_vars/host_vars or role defaults.

deploy.yml
update.yml

roles/docker_app/
templates/docker-compose.yml.j2

and:
Ansible/playbooks/update.yml
Ansible/roles/docker_app/tasks/main.yml
community.docker.docker_compose_v2


community.docker = the Ansible Collection providing Docker-related modules/plugins
docker_compose_v2 = the specific Ansible module used to control Docker Compose V2
"V2" refers to Docker Compose V2, which is the modern Compose implementation integrated into the Docker CLI.



### 5. PROJECT ROLE
cat Ansible/roles/docker_app/defaults/main.yml
cat Ansible/roles/docker_app/vars/main.yml
cat Ansible/roles/docker_app/tasks/main.yml
cat Ansible/roles/docker_app/handlers/main.yml
cat Ansible/roles/docker_app/meta/main.yml
cat Ansible/roles/docker_app/templates/docker-compose.yml.j2


defaults/main.yml                 # Defines configurable defaults.
vars/main.yml                     # This is fine; it simply means the role has no role-specific high-precedence vars here.
tasks/main.yml
    Creates /opt/... directory
    Logs into GHCR
    Generates docker-compose.yml from the template
    Starts/updates the Compose application
    Pulls the image

handlers/main.yml                 # Restarts the Compose application when the template changes.
meta/main.yml                     # Describes the role and its Ansible/Galaxy metadata.
templates/docker-compose.yml.j2   # Defines the actual deployed Compose configuration.


cat Ansible/roles/docker_app/defaults/main.yml
---
app_name: istrosec
app_environment: development
app_image: ghcr.io/metjumetju/istrosec:main
app_container_name: "{{ app_name }}-{{ inventory_hostname }}"
app_container_port: 5000
app_host_port: "{{ app_container_port }}"
app_project_dir: "/opt/{{ app_name }}-{{ inventory_hostname }}"
app_restart_policy: unless-stopped
app_registry: ghcr.io

cat Ansible/roles/docker_app/vars/main.yml
---
# vars file for roles/docker_app

cat Ansible/roles/docker_app/tasks/main.yml
---
- name: Create application directory
  ansible.builtin.file:
    path: "{{ app_project_dir }}"
    state: directory
    owner: root
    group: root
    mode: "0755"

- name: Log in to GitHub Container Registry
  community.docker.docker_login:
    registry_url: "{{ app_registry }}"
    username: "{{ vault_registry_username }}"
    password: "{{ vault_registry_token }}"
    reauthorize: true
  no_log: true

- name: Deploy Docker Compose configuration
  ansible.builtin.template:
    src: docker-compose.yml.j2
    dest: "{{ app_project_dir }}/docker-compose.yml"
    owner: root
    group: root
    mode: "0644"
  notify: Restart application

- name: Start application with Docker Compose
  community.docker.docker_compose_v2:
    project_src: "{{ app_project_dir }}"
    state: present
    pull: always

cat Ansible/roles/docker_app/handlers/main.yml
---
- name: Restart application
  community.docker.docker_compose_v2:
    project_src: "{{ app_project_dir }}"
    state: restarted

cat Ansible/roles/docker_app/meta/main.yml
---
galaxy_info:
  author: Mates
  description: Deploy the IstroSec application using Docker Compose
  license: MIT
  min_ansible_version: "2.14"

  platforms:
    - name: EL
      versions:
        - "9"

  galaxy_tags:
    - docker
    - compose
    - deployment
    - web

cat Ansible/roles/docker_app/templates/docker-compose.yml.j2
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
  {{ app_name }}:
    image: {{ app_image }}
    container_name: {{ app_container_name }}
    restart: {{ app_restart_policy }}
    ports:
      - "{{ app_host_port }}:{{ app_container_port }}"
    environment:
      APP_ENV: "{{ app_environment }}"
    volumes:
      - certs:/certs:ro
    depends_on:
      bootstrap:
        condition: service_completed_successfully
    pull_policy: always
volumes:
  certs:

### 6. PROJECT ROLE TESTS/DOC
cat Ansible/roles/docker_app/tests/inventory
cat Ansible/roles/docker_app/tests/test.yml
cat Ansible/roles/docker_app/README.md

cat Ansible/roles/docker_app/tests/inventory
localhost

cat Ansible/roles/docker_app/tests/test.yml
---
- hosts: localhost
  remote_user: root
  roles:
    - roles/docker_app

cat Ansible/roles/docker_app/README.md


### 7. EXTERNAL DOCKER ROLE
cat Ansible/roles/geerlingguy.docker/defaults/main.yml
cat Ansible/roles/geerlingguy.docker/handlers/main.yml
cat Ansible/roles/geerlingguy.docker/meta/main.yml
cat Ansible/roles/geerlingguy.docker/tasks/main.yml
cat Ansible/roles/geerlingguy.docker/tasks/docker-compose.yml
cat Ansible/roles/geerlingguy.docker/tasks/docker-users.yml

cat Ansible/roles/geerlingguy.docker/defaults/main.yml
cat Ansible/roles/geerlingguy.docker/handlers/main.yml
cat Ansible/roles/geerlingguy.docker/meta/main.yml
cat Ansible/roles/geerlingguy.docker/tasks/main.yml
cat Ansible/roles/geerlingguy.docker/tasks/docker-compose.yml
cat Ansible/roles/geerlingguy.docker/tasks/docker-users.yml

### 8. EXTERNAL DOCKER ROLE OS TASKS
cat Ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml
cat Ansible/roles/geerlingguy.docker/tasks/setup-RedHat.yml
cat Ansible/roles/geerlingguy.docker/tasks/setup-Suse.yml
cat Ansible/roles/geerlingguy.docker/vars/main.yml
cat Ansible/roles/geerlingguy.docker/vars/Alpine.yml
cat Ansible/roles/geerlingguy.docker/vars/Archlinux.yml
cat Ansible/roles/geerlingguy.docker/vars/Debian.yml
cat Ansible/roles/geerlingguy.docker/vars/RedHat.yml
cat Ansible/roles/geerlingguy.docker/vars/Suse.yml