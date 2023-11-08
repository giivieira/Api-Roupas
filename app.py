from flask import Flask

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def pagina_inicial():
    return 'Bem-vindo (a) à minha API de roupas!!!'

if __name__ == '__main__':
    app.run(debug=True)