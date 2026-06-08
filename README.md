# Cadastro de Clínicas

Sistema de cadastro de clínicas veterinárias desenvolvido como desafio técnico utilizando Flask, HTML, CSS e JavaScript.

## Sobre o Projeto

A aplicação permite o cadastro de clínicas veterinárias através de um formulário simples e intuitivo. Ao informar um CEP válido, o sistema consulta automaticamente a API ViaCEP para preencher os dados de endereço.

Além do cadastro, as clínicas registradas podem ser visualizadas diretamente na aplicação.

## Funcionalidades

- Cadastro de clínicas veterinárias
- Consulta automática de CEP via API ViaCEP
- Preenchimento automático de endereço
- Validação de CEP inválido ou não encontrado
- Listagem das clínicas cadastradas
- Persistência dos dados utilizando arquivo JSON

## Tecnologias Utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript
- ViaCEP API
- JSON

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/vet-clinic-manager.git
```

### 2. Acesse a pasta do projeto

```bash
cd Cadastro-clinicas
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

### 6. Acesse no navegador

```text
http://localhost:5000
```

## API Utilizada

ViaCEP

```text
https://viacep.com.br/
```

Utilizada para consulta automática de endereços a partir do CEP informado pelo usuário.

## Autor

Gustavo Cassettari Junior

- LinkedIn: https://www.linkedin.com/in/gustavo-cassettari-junior
- GitHub: https://github.com/GustavoCJr
