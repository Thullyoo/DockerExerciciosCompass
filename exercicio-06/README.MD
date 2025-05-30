## Exercício 6 

Utilize um multi-stage build para otimizar uma aplicação Go, reduzindo o tamanho da imagem final. Utilize para praticar o projeto [GS PING](https://github.com/docker/docker-gs-ping) desenvolvido em Golang.

1- Criação do Dockerfile

```
## BUILDER
# Associamos essa fase como builder, pois nela iremos gerar a build principal
FROM golang:1.19 AS builder

# Direcionamos o workdir para /app
WORKDIR /app

# Copiamos os arquivos de dependências do GO e instalamos as dependências
COPY go.mod go.sum ./
RUN go mod download

# Copiamos o código fonte GO e geramos a build
COPY *.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /gs-ping

## TESTS
# Associamos essa fase como tester, pois nela é feito os testes antes de executar a build
FROM golang:1.19 AS tester
RUN go test -v ./...

## EXECUTE BUILD
# Associamos essa fase como runner, pois nela será feita a execução principal da build gerada
FROM alpine:3.21.3 AS runner

# Direcionamos o workdir para /prod
WORKDIR /prod

# Copiamos o binário da build gerada anteriormente pelo builder e jogamos para a pasta /docker-gs-ping
COPY --from=builder /gs-ping /docker-gs-ping

# Expondo a porta 8080 para verificar a aplicação
EXPOSE 8080

# Executamos a build
CMD [ "/docker-gs-ping" ]
```

2- Gerar a imagem do Dockerfile

``` 
docker build -t testego:v1 .
```

3- Executar o container com a imagem gerada

```
docker run -p 8080:8080 --name teste_go testego:v1
```

4- Verificar no http://localhost:8080

![Imagem do site](image1.png)