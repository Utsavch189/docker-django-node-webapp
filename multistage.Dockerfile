# Dockerfile
# docker build -t utsav123/multistage-django . -f multistage.Dockerfile 

FROM python:3.10.12-alpine as base

RUN apk add --update --virtual .build-deps \
    build-base \
    python3-dev \
    libpq

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Final image, just copy over pre-compiled files

FROM python:3.10-alpine
RUN apk add libpq
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
WORKDIR /app
COPY . .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
