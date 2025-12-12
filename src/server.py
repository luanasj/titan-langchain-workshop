from flask import Flask,jsonify,request
from .llm import agent
from flask_cors import CORS 

app = Flask(__name__)

CORS(app) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/question")
def hello_llm():
# pega o parâmetro "text" da URL
    pergunta = request.args.get("text", "")

    resposta = agent.invoke({"messages":[{"role":"user", "content":pergunta}]})

    
    return jsonify({
            "pergunta_recebida": pergunta,
            "resposta": resposta["messages"][-1].content,
            "status": "sucesso"
        })
