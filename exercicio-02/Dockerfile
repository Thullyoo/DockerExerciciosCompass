FROM nginx:stable-alpine3.21-perl
RUN apk add --no-cache git
RUN rm -rf /usr/share/nginx/html/*
RUN git clone https://github.com/Thullyoo/formulario-page-html-css-dribbleinsp.git /usr/share/nginx/html/
EXPOSE 80
