# django-webapp
## Docker build [create image]
docker build . -t imagename

## run docker container
docker run imagename
### Or
docker run -d --name container_name imagename

## docker container kill and start and remove
docker kill container_id/container_name <br/>
docker stop container_id/container_name <br/>
docker start container_id/container_name <br/>
docker rm container_id/container_name

## see running conatiners
docker ps

## port maping with our local machine to container
 docker run -d -p localMachinePort:containerExposedPort appname
