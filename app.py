from flask import Flask, render_template, request, jsonify
import requests
from services.funcoes import (
    salvar_banco,
    ler_banco,
    validar_cep
)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/cadastrar-clinica", methods=['POST'])
def cadastrar_clinica():
    dados_clinica = request.form.to_dict()
    #fazer validações
    dados_antigos = ler_banco()
    #Fazer tratamento de erros
    dados_antigos.append(dados_clinica)
    salvar_banco(dados_antigos)
    return "Clinica cadastrada com sucesso!"

@app.route("/buscar_cep", methods=['POST'])
def buscar_cep():
    dados = request.get_json()
    cep = dados.get('cep')
    cep_sem_masc = cep.replace("-", "")
    erro = validar_cep(cep_sem_masc)
    if erro["erro"] == True:
        return erro["mensagem"]
    else:
        resposta = requests.get(
            f"https://viacep.com.br/ws/{cep_sem_masc}/json/"
        )
        dados_endereco = resposta.json()
        if "erro" in dados_endereco:
            return jsonify({"erro": "CEP inexistente"}), 404
        return jsonify(dados_endereco)


if __name__ == '__main__':
    app.run(debug=True)