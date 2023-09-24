# pull the official base image
FROM python:3.10.12-alpine

RUN mkdir django-webapp
# set work directory
WORKDIR /django-webapp

ADD . /django-webapp

# install dependencies
RUN pip install -r requirements.txt



EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# to create image --> docker build . -t appname
# from image to containers --> docker run -d -p port-n:8000 appname
