from flask import Flask, render_template, request
import banco_dados
import random

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar_produto", methods=['POST'])
def cadastrar_dados():
    nome_p = request.form['nome_produto']
    cpf = request.form['cpf_doador']
    quant = request.form['quantidade']
    data_val = request.form['data_validadde'] 
    
   
    valor = f"{quant} kg / {um}" if 'um' in locals() else f"{quant} kg / {request.form['unidade']}"
    
    um = request.form['unidade']
    
    print("Chegou")

    id = random.randint(102, 1000000000)
    resposta = banco_dados.insere_produto(id, nome_p, cpf, data_val, valor, um, quant)
    mensagem = ""
    if resposta == "Sucesso":
        mensagem = "Dados Salvos com Sucesso!"
    else:
        mensagem = "Erro ao registrar os produtos!"
    return render_template("cadastro.html", concluido=mensagem)

@app.route("/visualizar")
def visualizar_estoque():
    return render_template("visualizacao.html", lista_produtos = banco_dados.busca_todos_produtos())


if __name__ == "__main__":
    app.run(debug=True)