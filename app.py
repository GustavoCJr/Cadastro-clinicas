from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from services.funcoes import (
    salvar_banco,
    ler_banco,
    validar_cep
)
import json
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/cadastrar-clinica", methods=['POST'])
def cadastrar_clinica():
    dados_clinica = request.form.to_dict()
    for dado in dados_clinica.values():
        if not dado:
            return jsonify({"erro": "Dados incompletos"})
    dados_antigos = ler_banco()
    dados_antigos.append(dados_clinica)
    salvar_banco(dados_antigos)
    return redirect(url_for('listar_clinicas'))

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
            return jsonify({"erro": "CEP inexistente"})
        return jsonify(dados_endereco)

@app.route("/clinicas_cadastradas")
def listar_clinicas():
    clinicas = ler_banco()
    return render_template('clinicas.html', lista_de_clinicas= clinicas)

if __name__ == '__main__':
    app.run(debug=True)