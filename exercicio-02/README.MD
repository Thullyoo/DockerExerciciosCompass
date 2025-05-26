## Exercício 2

Crie um container com Nginx que sirva uma página HTML customizada (index.html). Monte um volume local com esse arquivo para que ele apareça na raiz do site (/usr/share/nginx/html). Acesse a página via http://localhost.

1- Criação do Dockerfile
```Dockerfile
FROM nginx:stable-alpine3.21-perl
RUN apk add --no-cache git
RUN rm -rf /usr/share/nginx/html/*
RUN git clone https://github.com/Thullyoo/formulario-page-html-css-dribbleinsp.git /usr/share/nginx/html/
EXPOSE 80
```

2- Gerar a build da Image do Dockerfile

```
docker build -t exercicio02:1.0 .
```

3- Executar o container com a imagem gerada

```
docker run -d -p 8080:80 --name exercicio02 exercicio02:1.0
```