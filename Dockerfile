# pull the official base image
FROM python:3.10.12-alpine

# set work directory
WORKDIR /usr/app

ADD requirements.txt . 
# means if requirements.txt changes then only build command install requirements.txt otherwise not

# install dependencies
RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

