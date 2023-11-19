FROM node:16.20.2-slim



RUN apt-get update -y && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package.json ./
RUN npm cache verify

RUN npm install 

COPY . .

CMD ["npm", "run", "serve"]