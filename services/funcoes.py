import json
import os
ARQUIVO_BD = 'data/banco.json'

def ler_banco():
    if not os.path.exists(ARQUIVO_BD):
        return []
    else:
        with open(ARQUIVO_BD, 'r', encoding='utf-8') as file:
            return json.load(file) 

def salvar_banco(dados):
    with open(ARQUIVO_BD, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

def validar_cep(cep):
    if not cep:
        return {
            "erro": True,
            "mensagem": "CEP vazio"
            }
    elif len(cep) != 8 or not cep.isdigit():
        return {
            "erro": True,
            "mensagem": "CEP inválido"
            }
    else:
        return {"erro": False}