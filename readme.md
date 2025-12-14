Esse repositório contém um exemplo mínimo de bot de llm usando langchain e groq provider integrando flask, html/js/css e whatsappweb-js.

## Tecnologias Necesárias
- Python + Pip
- Node 
- IDE (ex: vscode)

## Ambiente

### Ambiente Virtual Python
Cria ambiente:
```bash
python -m venv <nome-da-venv>
```
Inicia:
```bash
<nome-da-venv>\Scripts\activate
```
### Variáveis de Ambiente

Renomeie o .env.example como .env e preencha com a sua chave de API.

* gere a sua chave de API em 'https://console.groq.com/keys'

## Instalação de Dependências
Use esses dois comandos no terminal:

```bash
pip install -U -r requirements.txt
```

```bash
npm install
```

## Consumo do bot

### Inicie o Web Server Flask

```bash
flask --app src\server run
```

### Inicie o Whatsapp bot
```bash
node whatsapp.js
```
### Consuma no Navegador
    - Para usar a interface web acesse o arquivo index.html através do caminho do arquivo ou use a extensão Live Server.
