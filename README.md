# django-webapp
## Docker build [create image]
docker build . -t imagename

## run docker container
docker run imagename
### Or
docker run -d --name container_name imagename

## docker container kill and start and remove
docker kill container_id__
docker start container_id__
docker rm container_id

## see running conatiners
docker ps

## create containers
 docker run -d -p port:8000 appname
