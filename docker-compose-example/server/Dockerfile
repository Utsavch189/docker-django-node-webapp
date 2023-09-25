FROM node:alpine

WORKDIR /usr/app

ADD package*.json .

RUN npm install

ADD . .

EXPOSE 8000

CMD ["npm","run","start"]