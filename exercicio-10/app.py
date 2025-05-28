from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá do Contêiner Docker! Aplicação simples rodando."

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)