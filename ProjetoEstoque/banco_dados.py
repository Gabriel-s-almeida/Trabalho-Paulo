import sqlite3


conexao = sqlite3.connect("estoque.db")
CRIAR_TABELA_PRODUTO = '''create table if not exists produto(
    id int primary key, 
    nome_produto text, 
    cpf text,
    data_validade text, 
    valor text,
    unidade text
)'''
conexao.execute(CRIAR_TABELA_PRODUTO)
conexao.close()

def insere_produto(id, nome_produto, cpf, data_validade, valor, unidade, quant):
    conexao = sqlite3.connect("estoque.db")
    

    COMANDO_INSERE_PRODUTO = '''insert into produto(id, nome_produto, cpf, data_validade, valor, unidade) 
                                values (?,?,?,?,?,?)'''
    
    comando = conexao.cursor()
    comando.execute(COMANDO_INSERE_PRODUTO, (id, nome_produto, cpf, data_validade, valor, unidade))
    
    conexao.commit()
    conexao.close()
    return "Sucesso"

def busca_todos_produtos():
    conexao = sqlite3.connect("estoque.db")
    SELECT = "select id, nome_produto, cpf, data_validade, valor from produto"
    
    executador = conexao.cursor()
    executador.execute(SELECT)
    dados = executador.fetchall()
    conexao.close()
    return dados




