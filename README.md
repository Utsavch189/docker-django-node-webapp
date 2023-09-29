# Docker build [create image]
docker build . -t imagename

## see images
docker images

## run docker container
docker run imagename
### Or
docker run -d --name container_name imagename

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

## Go inside of a docker container from termial and access it like ssh
sudo docker exec -it container_id/container_name sh

## Pull docker images like, mongo,postgress,python,ubuntu which are already exists in docker hub
docker pull imagename(from docker hub)[with its version (Optional)]

# Docker Volume 

If we create an image of our application and run the container from that image, then it is fine. But <br/>
in dev mode if we make changes then the running container can't reflect that changes until we rebuild <br/>
our image again. So, here comes out Volume in docker, which map that container from our local machine <br/>
rather than image and changes will be reflected.

## Create a container with local machine map for live changes with Volume
docker run -v localWorkingDir:dockerWorkingDir --name containerName -p mappingPort:dockerImagePort imagename <br/>
<b>For this app</b> : docker run -v /home/utsav/Desktop/docker-django-webapp:/usr/app --name conty  -p 2800:8000 dj-app <br/>

suppose a dir inside of a image is mandatory to be present but that dir is missing in our <br/>
local working dir. That case if we create volume container above manner that dir inside of image <br/>
working dir should be gone because that dir is not present in our working dir. <br/>
<b>Here we should use : </b> docker run -v /home/utsav/Desktop/docker-django-webapp:/usr/app -v /usr/app/thatNeededDir --name conty  -p 2800:8000 dj-app <br/>
<b>For node apps create volume : </b> docker run -v pwd:/usr/app -v /usr/app/node_modules --name conty  -p port:exposedPort imagename <br/>
<b>** For React app -it flag should be appended before imagename</b><br/>

# Docker Compose
<b>
If we have some api servers and some client side apps then every time Dockerfile writing is overwhelming.<br/>
So docker compose is a global yaml file that helps to configure multiple containers. </b>

## Compose up 
docker-compose up --build
### Or
docker-compose up
