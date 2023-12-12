# dev
FROM node:16.20.2-slim as build-stage
RUN apt-get update -y && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY frontend/package.json /app/
RUN npm cache verify
RUN npm install
COPY frontend /app/
ENV NODE_ENV=production
RUN npm run build
# CMD ["npm", "run", "build"]
# prod
FROM nginx:stable-alpine3.17-slim as production-stage
COPY nginx/prod.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /dist/
COPY --from=build-stage /app/ssh /ssh/
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]