### DCA EXAM


https://www.itexams.com/exam/DCA

- 55 questions, 90 minutes, 13 multiple choice, 42 DOMC (discrete option multiple choice)

### 50 EXAMPLES OF THEM:

##### 1. Which two statements about Dockerfile COPY and ADD are correct?
    A. ADD can extract local compressed archives
    B. COPY can download files from HTTP URLs
    C. ADD supports remote URLs
    D. COPY automatically extracts tar archives
    E. COPY is generally preferred when only copying local files
    Answer: A, E
    ADD can extract local compressed archives, COPY is generally preferred when only copying local files

##### 2. Which command creates a new container from an image and starts it?
    A. docker create
    B. docker start
    C. docker run
    D. docker exec
    Answer: docker run

##### 3. You want to see the processes currently running inside a container. Which command should you use?
    A. docker ps
    B. docker top
    C. docker inspect
    D. docker stats
    Answer: docker top

##### 4. Which Dockerfile instruction creates a new filesystem layer during the image build?
    A. CMD
    B. ENV
    C. RUN
    D. EXPOSE
    Answer: RUN

##### 5. Which command displays the layers that make up an image?
    A. docker image history
    B. docker image layers
    C. docker history layers
    D. docker inspect --layers
    Answer: docker image history

##### 6. A Dockerfile contains:
    FROM alpine
    RUN apk add curl
    RUN echo hello
    What is the main benefit of Docker's build cache?
    A. Containers start automatically after the build
    B. Previously completed build steps can be reused
    C. Images are automatically pushed to a registry
    D. Containers share the same writable filesystem
    Answer: Previously completed build steps can be reused

##### 7. Which command removes a stopped container?
    A. docker delete
    B. docker remove
    C. docker rm
    D. docker stop --rm
    Answer: docker rm

##### 8. You want to pass an environment variable to a container when it starts. Which option is correct?
    A. docker run --env NAME=value image
    B. docker run --variable NAME=value image
    C. docker run --environment-file NAME=value image
    D. docker run --set-env NAME=value image
    Answer: docker run --env NAME=value image

##### 9. Which Docker network driver is normally used for communication between containers on different Docker hosts in a Swarm?
    A. bridge
    B. host
    C. overlay
    D. none
    Answer: overlay

##### 10. What does publishing a container port do?
    A. Creates a Docker image port
    B. Maps a host port to a container port
    C. Makes the container privileged
    D. Creates an overlay network
    Answer: Maps a host port to a container port

##### 11. Which command creates a Docker volume?
    A. docker volume create data
    B. docker create volume data
    C. docker storage create data
    D. docker volume new data
    Answer: docker volume create data

##### 12. What happens to data stored only in a container's writable layer when that container is removed?
    A. It is automatically moved into a volume
    B. It remains in the registry
    C. It is normally lost
    D. It is copied to the Docker daemon
    Answer: It is normally lost

##### 13. Which command initializes a Docker Swarm manager?
    A. docker swarm create
    B. docker swarm init
    C. docker cluster init
    D. docker manager init
    Answer: docker swarm init

##### 14. Which command displays the nodes participating in a Swarm?
    A. docker swarm ls
    B. docker node ls
    C. docker cluster ls
    D. docker service nodes
    Answer: docker node ls

##### 15. You need three replicas of an nginx service. Which command is correct?
    A. docker service create --replicas 3 nginx
    B. docker service run --count 3 nginx
    C. docker service create --count 3 nginx
    D. docker swarm create --replicas 3 nginx
    Answer: docker service create --replicas 3 nginx

##### 16. What is the purpose of a Swarm service?
    A. To build Docker images
    B. To define and maintain a desired state for containers
    C. To store Docker registry credentials
    D. To replace Docker networks
    Answer: To define and maintain a desired state for containers

##### 17. Which command shows the tasks belonging to a Swarm service?
    A. docker service containers SERVICE
    B. docker service ps SERVICE
    C. docker service tasks SERVICE
    D. docker task ls SERVICE
    Answer: docker service ps SERVICE

##### 18. A Swarm service should run exactly one task on every eligible node. Which service mode should be used?
    A. replicated
    B. global
    C. singleton
    D. distributed
    Answer: global

##### 19. Which command deploys a stack from a Compose-format YAML file?
    A. docker compose deploy
    B. docker stack deploy
    C. docker swarm deploy
    D. docker service deploy
    Answer: docker stack deploy

##### 20. Which Docker object is specifically designed to store sensitive data such as passwords in Swarm?
    A. Config
    B. Secret
    C. Volume
    D. Label
    Answer: Secret

##### 21. Which mechanism isolates processes in containers from processes running outside the container?
    A. Linux namespaces
    B. Docker labels
    C. Docker volumes
    D. Image layers
    Answer: Linux namespaces

##### 22. What is the primary purpose of cgroups?
    A. Image signing
    B. Process and resource control
    C. DNS resolution
    D. Registry authentication
    Answer: Process and resource control

##### 23. Which command authenticates the Docker CLI against a registry?
    A. docker auth
    B. docker registry login
    C. docker login
    D. docker authenticate
    Answer: docker login

##### 24. You have built:
    docker build -t registry.example.com/myapp:1.0 .
    Which command uploads this image to the registry?
    A. docker upload registry.example.com/myapp:1.0
    B. docker send registry.example.com/myapp:1.0
    C. docker push registry.example.com/myapp:1.0
    D. docker publish registry.example.com/myapp:1.0
    Answer: docker push registry.example.com/myapp:1.0

##### 25. A Kubernetes Deployment contains:
    containers:
    name: web
    image: registry.example.com/web:2.0
    What does the image field specify?
    A. The Dockerfile Kubernetes should build
    B. The image Kubernetes should obtain and run
    C. The registry Kubernetes should create
    D. The Docker network Kubernetes should create
    Answer: The image Kubernetes should obtain and run

##### 26. Which command displays detailed information about a Docker container?
    A. docker ps
    B. docker inspect
    C. docker info
    D. docker details
    Answer: docker inspect

##### 27. Which command displays the logs generated by a container?
    A. docker output CONTAINER
    B. docker logs CONTAINER
    C. docker history CONTAINER
    D. docker events CONTAINER
    Answer: docker logs CONTAINER

##### 28. Which command starts an existing stopped container?
    A. docker run CONTAINER
    B. docker create CONTAINER
    C. docker start CONTAINER
    D. docker launch CONTAINER
    Answer: docker start CONTAINER

##### 29. Which command executes a command inside a running container?
    A. docker run
    B. docker exec
    C. docker attach
    D. docker command
    Answer: docker exec

##### 30. Which Dockerfile instruction defines the default command executed when a container starts?
    A. RUN
    B. CMD
    C. BUILD
    D. START
    Answer: CMD

##### 31. Which Dockerfile instruction specifies an executable that will always be run when the container starts?
    A. CMD
    B. ENTRYPOINT
    C. RUN
    D. EXEC
    Answer: ENTRYPOINT

##### 32. Which Dockerfile instruction sets an environment variable in the image?
    A. ENV
    B. VAR
    C. ARG
    D. EXPORT
    Answer: ENV

##### 33. Which Dockerfile instruction defines build-time variables?
    A. ENV
    B. ARG
    C. VAR
    D. BUILDENV
    Answer: ARG

##### 34. What does the EXPOSE instruction in a Dockerfile do?
    A. Publishes the port on the host
    B. Documents the port intended to be used by the container
    C. Creates a firewall rule
    D. Opens the port on the host automatically
    Answer: Documents the port intended to be used by the container

##### 35. Which command lists locally available Docker images?
    A. docker list
    B. docker images
    C. docker image list-all
    D. docker repositories
    Answer: docker images

##### 36. Which command downloads an image from a registry?
    A. docker fetch
    B. docker download
    C. docker pull
    D. docker get
    Answer: docker pull

##### 37. Which command changes an image tag without modifying the image contents?
    A. docker rename
    B. docker tag
    C. docker label
    D. docker version
    Answer: docker tag

##### 38. What is the purpose of a Docker image layer?
    A. To store incremental filesystem changes
    B. To store container network connections
    C. To store container logs
    D. To store registry passwords
    Answer: To store incremental filesystem changes

##### 39. What happens when a Docker container is created from an image?
    A. The image is modified directly
    B. A writable container layer is added above the image layers
    C. The image is deleted
    D. A new registry is created
    Answer: A writable container layer is added above the image layers

##### 40. Which command removes an image?
    A. docker image rm IMAGE
    B. docker image delete IMAGE
    C. docker remove-image IMAGE
    D. docker erase IMAGE
    Answer: docker image rm IMAGE

##### 41. Which Docker storage mechanism is managed by Docker and stored outside the container's writable layer?
    A. Volume
    B. Namespace
    C. Layer
    D. Tag
    Answer: Volume

##### 42. What is a bind mount?
    A. A mount that maps a host filesystem path into a container
    B. A Docker image layer
    C. A registry connection
    D. A Swarm network
    Answer: A mount that maps a host filesystem path into a container

##### 43. Which network driver connects containers through the host's networking stack?
    A. bridge
    B. overlay
    C. host
    D. macvlan
    Answer: host

##### 44. Which network driver is the default for standalone Docker containers?
    A. overlay
    B. bridge
    C. host
    D. none
    Answer: bridge

##### 45. Which command creates a custom Docker network?
    A. docker network create mynet
    B. docker create network mynet
    C. docker network new mynet
    D. docker net add mynet
    Answer: docker network create mynet

##### 46. Which command connects an existing container to a Docker network?
    A. docker network connect NETWORK CONTAINER
    B. docker network attach NETWORK CONTAINER
    C. docker connect NETWORK CONTAINER
    D. docker network join NETWORK CONTAINER
    Answer: docker network connect NETWORK CONTAINER

##### 47. What provides service discovery between services attached to the same user-defined Docker network?
    A. Docker's embedded DNS
    B. Docker Registry
    C. Dockerfile
    D. Docker volume driver
    Answer: Docker's embedded DNS

##### 48. Which Swarm command promotes a worker node to manager?
    A. docker node promote NODE
    B. docker swarm promote NODE
    C. docker manager add NODE
    D. docker node manager NODE
    Answer: docker node promote NODE

##### 49. Which command displays the configuration and status of a Swarm service?
    A. docker service inspect SERVICE
    B. docker service info SERVICE
    C. docker inspect service SERVICE
    D. docker swarm inspect SERVICE
    Answer: docker service inspect SERVICE

##### 50. Which command scales an existing Swarm service to five replicas?
    A. docker service scale SERVICE=5
    B. docker service replicas SERVICE=5
    C. docker service update --replicas 5 SERVICE
    D. docker swarm scale SERVICE 5
    Answer: docker service scale SERVICE=5