# 🐳 Exercícios de Docker

Este repositório contém uma coleção de **exercícios de Docker**. Cada exercício apresenta uma **pergunta/desafio** e sua **resposta**.

## Exercício 1

Crie um arquivo Dockerfile que utilize a imagem alpine como base e imprima a mensagem Olá, Docker! ao ser executada. Construa a imagem com o nome meu-echo e execute um container a partir dela:

1- Criação do Dockerfile
```Dockerfile
FROM alpine:3.21.3
CMD ["echo", "Olá, Docker!"]
```

2- Gerar a build da Image do Dockerfile

```
docker build -t meu-echo:1.0 .
```

3- Executar o container com a imagem gerada
```
docker run meu-echo:1.0
```

## Exercício 2

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
docker run -d -p 8080:80 -t exercicio02 exercicio02:1.0
```