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

## Exercício 3

Inicie um container da imagem ubuntu com um terminal interativo (bash). Navegue pelo sistema de arquivos e instale o pacote curl utilizando apt.

1- Executar um container com a imagem do ubuntu

```
docker run -it ubuntu:25.10 sh
```

2- Dentro do container realizar a atualização do ubuntu

```
apt update && apt upgrade
```

3- Instalar o curl

```
apt install curl
```

## Exercício 4
Suba um container do MySQL (pode usar a imagem mysql:5.7), utilizando um volume nomeado para armazenar os dados. Crie um banco de dados, pare o container, suba novamente e verifique se os dados persistem.

1- Criar o volume no qual o container irá armazenar:

```
docker create volume db_data
```

2- Executar um container com o MySql:5.7, associando sua senha de usuário e o volume criado:

```
docker run -d --name db_teste -e MYSQL_ROOT_PASSWORD=1234 -v db_data:/db/data mysql:5.7 
```

3- Entrar no terminal do linux do container:

```
docker exec -it db_teste sh
```

4- Dentro container acessar o mysql e criar o Database e inserir um valor:

```
mysql -u root -p
CREATE DATABASE db_teste;
use db_teste;
CREATE TABLE USERS(id int, name VARCHAR(20), idade int);
INSERT INTO USERS(id, name, idade) VALUES (1, "João", 25);
```

5- Parar o container:

```
docker stop db_teste
```

6- Subir o container novamente:

```
docker start db_teste
```

7- Verificar se o valor inserido no db persiste:

```
mysql -u root -p
use db_teste;
SELECT * FROM db_teste;
```