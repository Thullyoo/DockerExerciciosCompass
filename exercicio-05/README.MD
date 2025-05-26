## Exercício 5

Crie um container com a imagem alpine passando uma variável de ambiente chamada MEU_NOME com seu nome. Execute o container e imprima o valor da variável com o comando echo.

1- Executar um container com a imagem do alpine atribuindo uma variável MEU_NOME 

```
docker run -it -e MEU_NOME=Thullyo alpine:3.21.3
```

2- No terminal do container printar na tela a variável

```
echo $MEU_NOME
```