# GitLab CI/CD: Automated Docker Container Build and Deployment

### OFFICIAL DOCUMENTATION

    GitLab installation
    https://docs.gitlab.com/install/package/

    GitLab Runner installation
    https://docs.gitlab.com/runner/install/linux-repository/

    GitLab Runner registration
    https://docs.gitlab.com/runner/register/

    GitLab Rake documentation (task management and build automation tool written in Ruby)
    https://docs.gitlab.com/administration/raketasks/

    Predefined CI/CD variables reference
    https://docs.gitlab.com/ci/variables/predefined_variables/

    CI Lint API
    https://docs.gitlab.com/api/lint/

    Runner Executors
    https://docs.gitlab.com/runner/executors/

    Docker installation
    https://docs.docker.com/engine/install/

    Docker installation - Red Hat
    https://docs.docker.com/engine/install/rhel/

    Docker installation - Ubuntu
    https://docs.docker.com/engine/install/ubuntu/

    Docker RHEL repository
    https://download.docker.com/linux/rhel/docker-ce.repo

    GitLab Runner RPM repository script
    https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh

    GitLab Runner DEB repository script
    https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh


### TASK

##### Run GitLab Server + GitLab Runner + Docker on ONE local server

- GITLAB SERVER
    - Install GitLab Server on SERVER 1
    - Open GitLab in browser
    - Create a new empty project

- GITLAB RUNNER
    - Install GitLab Runner on SERVER 2
    - Register the Runner with your GitLab project
    - Make sure Runner is online/available

- HELLO WORLD APP
    - Create simple web application
    - Create Dockerfile

- GITLAB CI/CD
    - Create: .gitlab-ci.yml
    - Pipeline should:
        - run on GitLab
        - build Docker image
        - tag the image
        - optionally run/push the image

- BASIC PIPELINE
    - stage: build
    - script:
        - docker build -t hello-world .
        - docker images

- TEST
    - run the Docker container
    - access the web application

- FIREWALL POSSIBLE ISSUE
    - If Docker networking does not work:
        -nft flush ruleset
    - Then disable nftables:
        - systemctl disable nftables
        - systemctl stop nftables
    - Restart Docker:
        - systemctl restart docker
    - Docker will recreate its firewall/network rules.



### 1. CHECK OPERATING SYSTEM
    cat /etc/os-release     # for OS name and release
    uname -m                # for CPU architecture

### 2. INSTALL GITLAB SERVER (Omnibus GitLab)

    - omnibus refers to an all-in-one software package that bundles GitLab along with all its required dependencies
    - such as Ruby, PostgreSQL, Redis, and Nginx—into a single, platform-specific Linux installer

    Install prerequisites:

    RED HAT:
    sudo dnf install -y curl policycoreutils openssh-server perl

    UBUNTU:
    sudo apt update
    sudo apt install -y curl policycoreutils openssh-server perl

    Common:
    sudo systemctl enable --now sshd

    Add the GitLab repository

    RED HAT:
    curl --location "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh" | sudo bash
    UBUNTU:
    curl --location "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh" | sudo bash

    Install GitLab:

    RED HAT:
    sudo dnf install -y gitlab-ee
    UBUNTU:
    sudo apt install -y gitlab-ee

    ENABLE AND START GITLAB SUPERVISOR
    sudo systemctl start gitlab-runsvdir
    sudo systemctl enable gitlab-runsvdir
    sudo systemctl status gitlab-runsvdir
    sudo systemctl stop gitlab-runsvdir

    CHECK GITLAB COMPONENTS
    sudo gitlab-ctl status

    START GITLAB COMPONENTS IF NOT RUNNIG
    sudo gitlab-ctl start
    sudo gitlab-ctl status

    STOP GITLAB COMPONENTS:
    sudo gitlab-ctl stop

    RESTART GITLAB:
    sudo gitlab-ctl restart

    ENABLE GITLAB AT BOOT:
    sudo systemctl enable gitlab-runsvdir
    sudo systemctl status gitlab-runsvdir

    CHECK GITLAB ENVIRONMENT INFORMATION
    sudo gitlab-rake gitlab:env:info

    Common:
    sudo ss -lntp | grep -E ':80|:443'

### Configure

    Check GitLab URL:
    cat /etc/hosts
    sudo grep '^external_url' /etc/gitlab/gitlab.rb

    Set it and reconfigure GitLab if differ:
    sudo EXTERNAL_URL="http://YOUR_SERVER_IP" gitlab-ctl reconfigure

    sudo gitlab-ctl status
    curl -v http://127.0.0.1/-/health
    curl -v http://127.0.0.1/-/readiness
 
    Open:
    http://YOUR_SERVER_IP

    CHECK FOR INITIAL PASSWORD (default user: root)
    sudo cat /etc/gitlab/initial_root_password
    
    CHECK FOR USERS
    sudo gitlab-rails console
        User.all
        User.pluck(:username, :email)
        User.find_by_username('root')


    OPTIONAL: CREATE GITLAB USER
    sudo gitlab-rails console

    Create the user:
    user = User.new(
    username: 'user_name',
    name: 'your_name',
    email: 'user@localhost',
    password: 'CHANGE_THIS_PASSWORD',
    password_confirmation: 'CHANGE_THIS_PASSWORD'
    )

### 3. INSTALL GITLAB RUNNER

    Add repository:

    RED HAT:
    curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh" -o script.rpm.sh
    sudo bash script.rpm.sh

    UBUNTU:
    curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" -o script.deb.sh
    sudo bash script.deb.sh

    Install:

    RED HAT:
    sudo dnf install -y gitlab-runner
    rpm -q gitlab-ee

    UBUNTU:
    sudo apt install -y gitlab-runner
    dpkg -l | grep gitlab
    
    START RUNNER:
    sudo systemctl start gitlab-runner

    STOP RUNNER:
    sudo systemctl stop gitlab-runner

    RESTART RUNNER:
    sudo systemctl restart gitlab-runner

    ENABLE RUNNER AT BOOT:
    sudo systemctl enable gitlab-runner
    sudo systemctl status gitlab-runner

### Configure:

    Add gitlab-runner to Docker group
    sudo usermod -aG docker gitlab-runner
    sudo systemctl restart gitlab-runner

    Check:
    id gitlab-runner
    getent group docker
    sudo -u gitlab-runner docker ps


### 4. INSTALL DOCKER

    RED HAT:

    sudo dnf -y install dnf-plugins-core
    sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

    UBUNTU:

    sudo apt update
    sudo apt install -y ca-certificates curl

    Add the official Docker Ubuntu repository:
    https://docs.docker.com/engine/install/ubuntu/

    Install:

    RED HAT:
    sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    UBUNTU:
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    Common:

    sudo systemctl enable --now docker
    sudo systemctl status docker
    docker --version


### 5. CREATE GITLAB PROJECT

    Files:
    index.html
    Dockerfile
    .gitlab-ci.yml

    In Web UI - New Project:
    Group name: lab
    Project name: hello-world

    in CLI - Create the Git repository
    git init

    git config --global user.name "AUTHOR_NAME" # commit identity
    git config --global user.email "YOUR_EMAIL"
    git config --global user.name
    git config --global user.email

    git status
    git remote -v
    git remote add origin http://YOUR_GITLAB_URL/lab/hello-world.git
    git remote add origin http://192.168.0.215/lab/hello-world.git

    git status
    git ls-files .gitlab-ci.yml
    git log --oneline --all -- .gitlab-ci.yml
    git remote -v

    git add .
    git commit -m "Initial hello world application"
    git branch          # or: git branch --show-current
    git branch -M main  # -M: forcefully rename the current branch
    git push -u origin main


### CREATE GITLAB CI/CD FILE

.gitlab-ci.yml:

```code
stages:
- build

build:
  stage: build
  script:
    - docker build -t hello-world:$CI_COMMIT_SHORT_SHA .

# NOTES:
# - CI_COMMIT_SHORT_SHA	- Availability: Pre-pipeline - the first eight characters of CI_COMMIT_SHA
# - identifier for the Git commit that triggered the pipeline
```

### CREATE HELLO WORLD APPLICATION

index.html

```code
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World from GitLab CI/CD!</h1>
</body>
</html>
```

### CREATE DOCKERFILE

Dockerfile:

```code
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

### PUSH PROJECT

    git init
    git add .
    git commit -m "Initial hello world application"
    git branch -M main
    git remote add origin YOUR_GITLAB_REPOSITORY_URL
    git push -u origin main

### 6. Create/Register Runner

    Web UI

        Check Runner assignment in GitLab Web UI
        Open: lab / hello-world
        -> Settings
        -> CI/CD
        -> Runners
        Then create/register Runner for lab/hello-world
    
    Check Configuration file
        -> Code
        -> Repository
        -> .gitlab-ci.yml

    Check pipeline:
        Project
        -> Build
        -> Pipelines
        Click status icon -> build to see the actual Runner output

    Check/Create GitLab Personal Access Token (PAT)
        Avatar / profile
        -> Edit profile
        -> Access
        -> Personal access tokens
 
        Generate legacy token or Fine-grained personal access token
        - Legacy token:
            - is scoped to all groups and projects with broad permissions to resources.
        - Fine-grained personal access token:
            - give you granular control over the specific resources and actions available to the token.

        - For creating a pipeline via the REST API — the minimum scope you need is:
            - api

    Check project ID
        Project
        -> Settings
        -> General
        -> Project ID

    Create new Runner from Web UI
        Tags: leave empty
        Run untagged jobs: ENABLED
        Runner description: hello-world-runner
        Paused: DISABLED
        Protected: DISABLED
        Lock to current projects: ENABLED
        Maximum job timeout: leave empty

        NEXT SCREEN
        Register "hello-world-runner" runner
        Platform - Operating systems - Linux
        Copy and paste the following command into your command line to register the runner.

        After running this command (by sudo it would have registered the Runner in system mode):

        Enter the GitLab instance URL
        Enter a name for the runner. This is stored only in the local config.toml file
        Enter an executor: docker
        Enter the default Docker image (for example, ruby:3.3): docker:cli   
        NOTE: Configuration (with the authentication token) was saved in "/home/<user_name>/.gitlab-runner/config.toml"


    Check Runner from CLI

        Runner configuration file (config.toml) has:
        executor = "docker"
        [runners.docker]
        image = "docker:cli"
        privileged = true
        volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
        To view the runner, go to Project › CI/CD Settings › Runners

        sudo systemctl restart gitlab-runner
        sudo systemctl status gitlab-runner --no-pager
        sudo gitlab-runner verify

        Manually verify that the runner is available to pick up jobs
        sudo systemctl start gitlab-runner
        sudo gitlab-runner run --config /etc/gitlab-runner/config.toml   

        sudo gitlab-runner verify
        sudo gitlab-runner list
        sudo journalctl -u gitlab-runner -f

        Check GitLab access token
        sudo cat /etc/gitlab-runner/config.toml


### PIPELINE

    git push
    -> GitLab Server
    -> GitLab Runner
    -> .gitlab-ci.yml
    -> docker build -> Docker image

### TEST CONTAINER

    docker images
    docker run -d --name hello-world-test -p 8080:80 hello-world:TAG
    docker ps
    docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Names}}'
    curl http://localhost:8080


### FIREWALL

    sudo nft list ruleset

    Only if Docker networking is blocked:
    sudo nft flush ruleset
    sudo systemctl stop nftables.service
    sudo systemctl disable nftables.service
    sudo systemctl restart docker.service


### Registry
    sudo vi /etc/gitlab/gitlab.rb
    registry_external_url 'https://registry.example.com'
    sudo gitlab-ctl reconfigure
    sudo gitlab-ctl status

    sudo grep -R "registry_external_url" /etc/gitlab/gitlab.rb
    sudo gitlab-ctl status | grep registry
    cat /etc/hosts

### FINAL PROJECT FILES

    hello-world/
    index.html
    Dockerfile
    .gitlab-ci.yml