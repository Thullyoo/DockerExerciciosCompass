# Exercício 12

## Questão

12. Após identificar vulnerabilidades com ferramentas como o Trivy, o próximo passo é corrigi-las. Imagens grandes e genéricas frequentemente trazem bibliotecas desnecessárias e vulneráveis, além de usarem o usuário root por padrão. Neste exercício, você irá trabalhar com um exemplo de Dockerfile com más práticas e aplicar melhorias para construir uma imagem mais segura e enxuta. Identifique as melhorias e gere uma nova versão de Dockerfile.

---

### Arquivos Iniciais Fornecidos:

**Dockerfile (`Dockerfile vulnerável`)**

```dockerfile
# Dockerfile vulnerável
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

**requirements.txt**

```
flask==1.1.1
```
**app.py**
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

## Resolução

1. Modificar o Dockerfile

```
FROM python:3.9

WORKDIR /app 

COPY requirements.txt . 
RUN pip install -r requirements.txt  

RUN python -m pip install --upgrade setuptools  <- ATUALIZAMOS A VERSAO DO SETUPTOOLS PARA PREVINIR VULNERABILIDADES

RUN addgroup --gid 1234 teste && \  <-- CRIAMOS UM GRUPO PARA O NOVO USUARIO
    adduser --uid 1234 --ingroup teste --shell /bin/false --no-create-home --disabled-password thullyo <-- CRIAMOS O NOVO USUARIO
USER thullyo <-- REDIRECIONAMOS O USUARIO QUE VAI EXECUTAR O CÓDIGO

COPY . . 
CMD ["python", "app.py"]

EXPOSE 5000
```

2. Modificar versão do Flask requirido

**requirements.txt**
```
flask=3.1.1
```

3. Fazer o código rodar e escutar na porta 5000

**app.py**
```
from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def hello_world(): 
  return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
