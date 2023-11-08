from urllib import request

from fastapi import FastAPI, HTTPException, status, Response, Path
from models import Dog
import requests

app = FastAPI()

roupas = {
    {"id": 1,
     "nome:": "Camiseta",
     "categoria": "Rouopas Masculinas"},
    {"id": 2,
     "nome:": "Vestido",
     "categoria": "Rouopas Femininas"}
}

@app.get("/roupas")
async def get_roupas():
    return {"Message": [request.json(), roupas]}


#Rota para listar todas as roupas
@app.route

# Endpoint para listar roupas
@app.route('/roupas', methods=['GET'])
def listar_roupas():
    #Consumir a API aqui usando a biblioteca 'requests' e retornar os dados no formato JSON

#Endpoint para criar uma nova roupa
@app.route('/roupas', methods=['POST'])
def criar_roupa():
    #Receber os dados da nova roupa
    dados_roupa = request.json
    # Processar os dados e criar a nova roupa
    # Enviar a nova roupa para a API de roupas usando requests

#End point para atualizar uma roupa existente
@app.route('/roupas/<int;id_roupa>',
           methods=['PUT'])
def atualizar_roupa(id_roupa):
    #Receber os dados atualizados da roupa do corpo da solicitação (request)
    dados_atualizados = request.json
    # Atualizar a roupa com o ID fornecido na API de roupas
    # Retornar uma resposta adequada

    #Endpoint para excluir uma roupa
@app.route('/roupas/<int:id_roupa>', methods=['DELETE'])
def excluir_roupa(id_roupa):
# Excluir a roupa com o ID fornecido na API

if __name__ == '__main':
    app.run(debug=True)