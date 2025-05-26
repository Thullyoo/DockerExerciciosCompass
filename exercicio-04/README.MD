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