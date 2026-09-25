### DOCKER - MOST USED COMMANDS & OPTIONS

### IMAGES
    docker images                    List images
    docker image ls                  List images
    docker pull IMAGE                Download image
    docker push IMAGE                Upload image
    docker build -t NAME:TAG .       Build + tag image
    docker tag IMAGE NAME:TAG        Create/change image tag
    docker image rm IMAGE            Remove image
    docker image inspect IMAGE       Inspect image
    docker image history IMAGE       Show image layers

### CONTAINERS
    docker run IMAGE                 Create + start container
    docker create IMAGE              Create container only
    docker start CONTAINER            Start existing container
    docker stop CONTAINER             Stop container
    docker restart CONTAINER          Restart container
    docker kill CONTAINER             Force stop container
    docker rm CONTAINER               Remove container
    docker rm -f CONTAINER            Force remove container

### CONTAINER INFO
    docker ps                        Running containers
    docker ps -a                     All containers
    docker inspect CONTAINER         Detailed information
    docker logs CONTAINER            Container logs
    docker stats                     Resource usage
    docker top CONTAINER             Processes inside container
    docker port CONTAINER            Port mappings
    docker diff CONTAINER            Filesystem changes

### EXEC / TERMINAL
    docker exec CONTAINER CMD        Run command in running container
    docker exec -it CONTAINER bash   Interactive terminal
    docker attach CONTAINER          Attach to main process

### RUN OPTIONS
    -d                               Detached/background
    -i                               Keep STDIN open
    docker build -t                  -t =TAG
    docker run -t                    -t = TTY
    docker exec -t                   -t = TTY
    -p HOST:CONTAINER                Publish/map port
    -P                               Publish all exposed ports
    -e NAME=value                    Environment variable
    -v SOURCE:DEST                   Volume/bind mount
    --name NAME                      Container name
    --rm                             Remove container after exit
    --network NETWORK                Use network
    --restart POLICY                 Restart policy
    --privileged                     Extended privileges

### VOLUMES
    docker volume ls                 List volumes
    docker volume create NAME        Create volume
    docker volume inspect NAME       Inspect volume
    docker volume rm NAME            Remove volume
    docker volume prune              Remove unused volumes

### NETWORKS
    docker network ls                List networks
    docker network create NAME       Create network
    docker network inspect NAME      Inspect network
    docker network connect NET CONT  Connect container
    docker network disconnect NET CONT
    docker network rm NAME           Remove network

### NETWORK DRIVERS
    bridge                           Default standalone network
    host                             Host networking stack
    none                             No networking
    overlay                          Multi-host / Swarm

### DOCKERFILE
    FROM                             Base image
    RUN                              Build-time command
    COPY                             Copy files
    ADD                              Copy + extra features
    CMD                              Default runtime command
    ENTRYPOINT                       Main executable
    ENV                              Environment variable
    ARG                              Build-time variable
    EXPOSE                           Documents port
    WORKDIR                          Working directory
    USER                             User
    VOLUME                           Declare volume
    LABEL                            Metadata

### IMPORTANT DOCKERFILE
    RUN                              Build time
    CMD                              Default runtime command
    ENTRYPOINT                       Main executable
    ARG                              Build-time variable
    ENV                              Environment variable
    EXPOSE                           Does NOT publish port

### COMPOSE
    docker compose up                Start services
    docker compose up -d             Start in background
    docker compose down              Stop + remove
    docker compose ps                List services
    docker compose logs              Show logs
    docker compose exec SERVICE CMD  Execute command
    docker compose build             Build images
    docker compose pull              Pull images

### SWARM
    docker swarm init                Initialize manager
    docker swarm join                Join Swarm
    docker swarm leave               Leave Swarm

    docker node ls                   List nodes
    docker node inspect NODE         Inspect node
    docker node promote NODE         Worker -> manager
    docker node demote NODE          Manager -> worker

    docker service create nginx      Create service
    docker service ls                List services
    docker service ps SERVICE        Show service tasks
    docker service inspect SERVICE  Inspect service
    docker service logs SERVICE      Service logs
    docker service scale S=5         Scale service
    docker service rm SERVICE        Remove service

### SWARM SERVICE
    --replicas 3                     3 replicas
    --mode global                    1 task per eligible node

### STACKS
    docker stack deploy -c FILE NAME Deploy stack
    docker stack ls                  List stacks
    docker stack services NAME       List stack services
    docker stack ps NAME             List stack tasks
    docker stack rm NAME             Remove stack

### SECRETS / CONFIGS
    docker secret ls                 List secrets
    docker secret create NAME FILE   Create secret
    docker secret inspect NAME       Inspect secret
    docker secret rm NAME            Remove secret

### docker config ls                 List configs
    docker config create NAME FILE   Create config
    docker config inspect NAME       Inspect config
    docker config rm NAME            Remove config

### REGISTRY
    docker login                     Login to registry
    docker logout                    Logout
    docker pull IMAGE                Registry -> local
    docker push IMAGE                Local -> registry
    docker tag IMAGE REGISTRY/IMAGE  Tag for registry

### SYSTEM
    docker info                      Docker system information
    docker version                   Docker version
    docker system df                 Disk usage
    docker system prune              Clean unused resources

### COMMON FLAGS
    -a                               All
    -q                               Quiet / IDs only
    -f                               Force
    -d                               Detached
    -i                               Interactive
    -t                               TTY OR TAG (depends on command)
    -p                               Publish port
    -P                               Publish all exposed ports
    -e                               Environment variable
    -v                               Volume/bind mount