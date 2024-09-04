# Docker build [create image]
docker build . -t imagename

## see images
docker images

## run docker container
docker run imagename
### Or
docker run -d --name container_name imagename

# Some Keywords For Dockerfile..
1. From : Use to pull image with version </br>
2. RUN : RUN is an image build step, the state of the container after a RUN command will be committed to the container image.</br>
3. ENV : use to set enviroment vars</br>
4. LABEL : use to put more extra meta info into that image.<br/>
5. EXPOSE : The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. </br>
6. CMD : The CMD command​ specifies the instruction that is to be executed when a Docker container starts. </br>
7. COPY : use to just copying things.</br>
8. ADD :  ADD has some features (like local-only tar extraction and remote URL support) that are not immediately obvious. </br>
9. WORKDIR : The WORKDIR instruction in a Dockerfile sets the current working directory for subsequent instructions in the Dockerfile.</br>
10. ENTRYPOINT : Same as cmd but it executes before cmd. </br>


## Different between COPY and ADD in Dockerfile
<b>
COPY just copy things , but ADD do more stuffs.</br>
Suppose I COPY a .zip file into docker build it will simply copy that file, </br>
but in case of ADD that .zip will be extracted also while build.</br>
The best use for ADD is local tar file auto-extraction into the image, as in ADD rootfs.tar.xz / .
</b>

## docker container  run,kill and start and remove
docker run image_name [-d,--name are Optional but recomended according to me] (If that image present locally then it use it otherwise it search that image into docker hub)<br/>
docker kill container_id/container_name <br/>
docker stop container_id/container_name <br/>
docker start container_id/container_name <br/>
docker rm container_id/container_name

## see running conatiners
docker ps

## create container and port maping with our local machine to container
 docker run -d -p localMachinePort:containerExposedPort --name containername  imagename

## Docker Import and Export
docker export container_id/container_name > something.zip <br/>
doxker import - imageename < something.zip

## Docker commit
<b>
Docker commit is used to reflect changes of a container to a new image.
</b>
docker commit container_id imagename:tag</br>

## Docker save and load
1. docker save imagename > something.tar (works same as export but it stores every layer of that image)<br/>
2. docker load image < something.tar (works same as import but load the whole image with every data)

## Push Docker image to docker hub
1. docker login <br/>
2. docker tag imagename docker_hub_username/imagename <br/>
3. docker push docker_hub_username/imagename </br>

# Docker Registry/Repository
<b>
Docker registries are used to host and distribute Docker Images.</br>
Docker registry may be used to create faster CI/CD pipelines, which helps to reduce build and deployment time.</br> Docker Registry is useful if you want complete control over where your images are kept. A private Docker registry can be used.</br> You gain total control over your applications by doing so.
</b></br>

1. docker image pull registry:latest.</br>
2. docker container run -d -p 5000:5000 --name my-registry registry.</br>
3. docker image tag utsav123/django-push:latest 127.0.0.1:5000/utsav123/django-push:v2.</br>
4. docker image push 127.0.0.1:5000/utsav123/django-push:v2.</br>
5. If we hit http://127.0.0.1:5000/v2/_catalog , will see now : {"repositories":["utsav123/django-push"]}. </br>
<b>**note : docker registry only works on https. But by default 127.0.0.0/8 ranges are allowed. We can change this behaviour.</b></br>

## Allow other ip ranges for docker registry pull/push in http env (insecure):
1. create a file daemon.json.</br>
2. Put like this, {"insecure-registries":["10.10.10.1:5000"] }.</br>
3. move this to /etc/docker. </br>
4. service docker restart.</br>

## Allow docker registry pull/push in https env with ssl cert (secure):
1. if any daemon.json in /etc/docker/ , delete it.</br>
2. mkdir certs. (into /home/utsav/Desktop)</br>
3. openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt </br>
4. in that stage ,Common Name (e.g. server FQDN or YOUR name) []:repo.docker.local </br>
5. cp -r certs/ /etc/docker/certs.d </br>
6. cd /etc/docker/certs.d/ </br>
7. mkdir repo.docker.local:5000 </br>
8. cp /home/utsav/Desktop/certs/domain.crt /etc/docker/certs.d/repo.docker.local\:5000/ca.crt </br>
9. gedit /etc/hosts and update, 192.168.140.129 repo.docker.local </br>
10. service docker restart.</br>
11. docker container run -d --name secure_registry -p 5000:5000  -v $(pwd)/certs/:/certs -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key registry. (into /home/utsav/Desktop dir)</br>
12. Now instade http://127.0.0.1:5000 we can use https://repo.docker.local:5000

## Pull image from docker hub
docker pull imagename

## Go inside of a docker container from termial and access it like ssh
docker exec -it container_id/container_name sh</br>
<b>To enter conatiner with root user : </b> docker exec -it -u root container_id/container_name sh

## Pull docker images like, mongo,postgress,python,ubuntu which are already exists in docker hub
docker pull imagename(from docker hub)[with its version (Optional)]

# Docker Volume 
Volumes are the preferred mechanism for persisting data generated by and used by Docker containers. While bind mounts are dependent on the directory structure and OS of the host machine, volumes are completely managed by Docker.</br>
<b>When a container creates , a volume of that container generated automatically.</b></br>

1. Volumes are easier to back up or migrate than bind mounts.<br/>
2. You can manage volumes using Docker CLI commands or the Docker API.<br/>
3. Volumes work on both Linux and Windows containers.<br/>
4. Volumes can be more safely shared among multiple containers.<br/>
5. Volume drivers let you store volumes on remote hosts or cloud providers, to encrypt the contents of volumes, or to add other functionality.<br/>
6. New volumes can have their content pre-populated by a container.<br/>
7. Volumes on Docker Desktop have much higher performance than bind mounts from Mac and Windows hosts.<br/>

## Persist data of a mysql container,
1. docker image inspect imageid, and we will get something like, <b>"Volumes": {
                "/var/lib/mysql": {}
            },</b></br>
2. /var/lib/mysql denotes the target volume mount dir of that mysql image.</br>
3. docker volume create volname.</br>
4. docker run -d --name container_name -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v volname:/var/lib/mysql  mysql.</br>
<b>Now every changes inside mysql db should be stored inside of that volume.</br>
And if we del taht conatiner and create container again with same volume just like</br>
line number 4, every data should be persisted.
</b>

# Docker Bind-Mount
If we create an image of our application and run the container from that image, then it is fine. But <br/>
in dev mode if we make changes then the running container can't reflect that changes until we rebuild <br/>
our image again. So, here comes out Volume in docker, which map that container from our local machine <br/>
rather than image and changes will be reflected.

## Create a container with local machine map for live changes with bind-mount
docker run -v localWorkingDir:dockerWorkingDir --name containerName -p mappingPort:dockerImagePort imagename <br/>
<b>For this app</b> : docker run -v /home/utsav/Desktop/docker-django-webapp:/usr/app --name conty  -p 2800:8000 dj-app <br/>

suppose a dir inside of a image is mandatory to be present but that dir is missing in our <br/>
local working dir. That case if we create volume container above manner that dir inside of image <br/>
working dir should be gone because that dir is not present in our working dir. <br/>
<b>Here we should use : </b> docker run -v /home/utsav/Desktop/docker-django-webapp:/usr/app -v /usr/app/thatNeededDir --name conty  -p 2800:8000 dj-app <br/>
<b>For node apps I want to persist node_modules : </b> docker run -v localWorkingDir:/usr/app -v /usr/app/node_modules --name conty  -p port:exposedPort imagename <br/>
<b>** For React app -it flag should be appended before imagename</b><br/>

# Docker Network
By Default docker comes with bridge,host and null networks drivers.</br>
Any container by default runs with bridge network.</br>
Always it is best practice to use custom diff networks for diff applications.</br>
<b>A bridge network can connect multiple containers. But a host network only can connect a single container.</b></br>
<b>Host network attach the machines private ip to that container.</b></br>
<b>null network makes a container network-less.</b></br>

## Network Drivers
<b>
1. bridge: The default network driver. If you don't specify a driver, this is the type of network you are creating. Bridge networks are commonly used when your application runs in a container that needs to communicate with other containers on the same host.</br>

2. host: Remove network isolation between the container and the Docker host, and use the host's networking directly. Use your's machine's ip.</br>

3. overlay: Overlay networks connect multiple Docker daemons together and enable Swarm services and containers to communicate across nodes. This strategy removes the need to do OS-level routing.</br>

4. ipvlan: IPvlan networks give users total control over both IPv4 and IPv6 addressing. The VLAN driver builds on top of that in giving operators complete control of layer 2 VLAN tagging and even IPvlan L3 routing for users interested in underlay network integration.</br>

5. macvlan: Macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network. The Docker daemon routes traffic to containers by their MAC addresses.</br> Using the macvlan driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host's network stack.</br>

6. none: Completely isolate a container from the host and other containers. none is not available for Swarm services. </br>
</b>

## Network Drivers Summery
<b>
The default bridge network is good for running containers that don't require special networking capabilities.</br>
User-defined bridge networks enable containers on the same Docker host to communicate with each other. A user-defined network typically defines an isolated network for multiple containers belonging to a common project or component.</br>
Host network shares the host's network with the container. When you use this driver, the container's network isn't isolated from the host.</br>
Overlay networks are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using Swarm services.</br>
Macvlan networks are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.</br>
IPvlan is similar to Macvlan, but doesn't assign unique MAC addresses to containers. Consider using IPvlan when there's a restriction on the number of MAC addresses that can be assigned to a network interface or port.</br>
</b>


## Create Your Network
docker network create -d driver-type network-name.</br>
<b>Also we can assign ip and lot more things for our custom network.</b></br>

## Attach a container with network.
docker run --network=network-name image_name.</br>
<b>All containers in this network can communicate with each other without port mapping. But not for outer networks.</b></br>

## Connect/Disconnect a container with network.
dcoker network connect network-name container_id.</br>
dcoker network disconnect network-name container_id.</br>
<b>By connect method we can connect multiple networks to a container.</b></br>

# Docker Compose
<b>
If we have some api servers and some client side apps then every time Dockerfile writing is overwhelming.<br/>
So docker compose is a global yaml file that helps to configure multiple containers. </b>

## Compose image 
docker-compose build

### run those containers
docker-compose up -d

### Down or Remove those containers
docker-compose down or docker-compose down -v</br>
</br>
<b>Magic of docker-compose is because of we already mention container names into docker compose.yaml ,</br>
so we don't need to specify container names again and again to run and remove containers.</br>
</b>
<b>By default docker-compose searches for docker-compose.yml file on that dir</b>

## Compose with a diff named yml file
docker-compose -f filename.yml up -d

## extra-host config in docker-compose.yaml
<b><pre>
version: "3.10"
services:
  flask:
    build:
      context: .
      dockerfile: ./Dockerfile
    ports:
      - 8000:8000
    volumes:
      - /home/utsav/logs:/app/logs
    image: test_flask
    container_name: flask1
    extra_hosts:
      - "host.docker.internal:host-gateway"</pre>
</b>
<br>
### What is <b>extra_hosts: - "host.docker.internal:host-gateway"</b><br>
1. extra_hosts allows you to define additional host-to-IP mappings inside the container.<br>
2. "host.docker.internal:host-gateway" maps host.docker.internal to the host machine's IP address. This is especially useful if your containers need to communicate with services running on your host machine.<br>
### Use Case:
<b>You have a service running on your host machine (e.g., a database on port 5432),<br> and you want to connect to it from within a Docker container. The host.docker.internal alias allows the container to reach the host machine by this name.<b><br>
<b><pre>
import psycopg2

# Connect to a PostgreSQL database running on the host machine
connection = psycopg2.connect(
    host="host.docker.internal",
    port=5432,
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
</pre></b><br>
<b>
In this example, host.docker.internal will point to the host machine's IP address,<br>
allowing the Flask container to connect to the database running on the host. <br>
The extra_hosts setting in the Docker Compose file makes this possible.</b><br>

