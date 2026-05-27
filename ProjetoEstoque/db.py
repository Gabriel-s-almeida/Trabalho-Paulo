import sqlite3

nome_banco = "doadores.db"

def inicializar_banco():
    try:
        with sqlite3.connect(nome_banco) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS doador (
                    id INTEGER PRIMARY KEY,
                    nome_doador TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    data_nascimento TEXT,
                    peso TEXT
                )
            """)
            print("Banco e tabela de doadores prontos!")
    except sqlite3.Error as e:
        print(f"Erro ao criar banco: {e}")

def escrever_dados(id, nome, cpf, data_nascimento, peso):
    try:
        with sqlite3.connect(nome_banco) as conexao:
            cursor = conexao.cursor()
            
            sql = "INSERT INTO doador (id, nome_doador, cpf, data_nascimento, peso) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql, (id, nome, cpf, data_nascimento, peso))
            print(f"Doador {nome} inserido com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: O ID ou CPF já existe no banco.")
    except sqlite3.Error as e:
        print(f"Erro ao escrever: {e}")

def ler_dados():
    print("\n--- Lista de Doadores no Banco ---")
    try:
        with sqlite3.connect(nome_banco) as conexao:
            cursor = conexao.cursor()
           
            cursor.execute("SELECT id, nome_doador, cpf, data_nascimento, peso FROM doador")
            rows = cursor.fetchall()
            
            for row in rows:
                print(f"ID: {row[0]} | Nome: {row[1]} | CPF: {row[2]} | Nasc: {row[3]} | Peso: {row[4]}kg")
    except sqlite3.Error as e:
        print(f"Erro ao ler: {e}")

if __name__== "__main__":
    inicializar_banco()
    
    escrever_dados(101, "Alice Silva", "111.111.111-11", "1995-05-12", "65")
    escrever_dados(102, "Bruno Costa", "222.222.222-22", "1992-08-24", "78")
    
    ler_dados()