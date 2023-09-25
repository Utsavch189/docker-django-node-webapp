FROM node:alpine

WORKDIR /usr/app

ADD package*.json .

RUN npm install

ADD . .

EXPOSE 3000

CMD ["npm","start"]