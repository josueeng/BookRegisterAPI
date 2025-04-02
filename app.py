# Importação das bibliotecas necessárias
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Caminho absoluto para o banco de dados
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database.db")

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)

# Função para inicializar o banco de dados
def init_db():
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS LIVROS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                image_url TEXT NOT NULL
            )
            """
        )
        conn.commit()  # Garante que as alterações sejam salvas

# Inicialização do banco de dados
init_db()

# Rota para cadastrar um novo livro
@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    # Verifica se todos os campos obrigatórios foram preenchidos
    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    # Insere o livro no banco de dados
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute(
            """
            INSERT INTO LIVROS (titulo, categoria, autor, image_url)
            VALUES (?, ?, ?, ?)
            """,
            (titulo, categoria, autor, image_url)
        )
        conn.commit()  # Salva as alterações no banco de dados
    return jsonify({"Mensagem": "Livro cadastrado com sucesso!"}), 201

# Rota para listar todos os livros
@app.route("/livros", methods=["GET"])
def listar_livros():
    with sqlite3.connect(DATABASE_PATH) as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()
        livros_formatados = [
            {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4]
            }
            for item in livros
        ]
    return jsonify(livros_formatados), 200

# Início do servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
