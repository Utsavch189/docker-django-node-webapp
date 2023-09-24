# django-webapp
## Docker build [create image]
docker build . -t imagename

## run docker container
docker run imagename
     ### Or,
docker run -d --name container_name imagename

## see running conatiners
docker ps

## create containers
 docker run -d -p port:8000 appname
