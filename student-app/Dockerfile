FROM node:lts-alpine

WORKDIR /usr/src/vite

COPY package*.json ./
RUN npm ci

COPY . .

CMD ["npm", "run", "dev"]