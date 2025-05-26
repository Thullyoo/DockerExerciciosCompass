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