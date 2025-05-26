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