from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Cria o banco e a tabela
def criar_tabela():
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

criar_tabela()

# Funções de banco
def adicionar_usuario(nome, email):
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def buscar_usuario_por_nome(nome):
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", ('%' + nome + '%',))
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def atualizar_usuario(id, nome, email):
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
    conexao.commit()
    conexao.close()

def deletar_usuario(id):
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

# Rotas
@app.route("/", methods=["GET", "POST"])
def index():
    usuarios = []
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        adicionar_usuario(nome, email)
        return redirect(url_for("index"))

    return render_template("index.html", usuarios=usuarios)

@app.route("/buscar", methods=["POST"])
def buscar():
    nome = request.form.get("nome_busca")
    usuarios = buscar_usuario_por_nome(nome)
    return render_template("index.html", usuarios=usuarios)

@app.route("/listar")
def listar():
    usuarios = listar_usuarios()
    return render_template("index.html", usuarios=usuarios)

@app.route("/deletar/<int:id>")
def deletar(id):
    deletar_usuario(id)
    return redirect(url_for("listar"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        atualizar_usuario(id, nome, email)
        return redirect(url_for("listar"))

    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conexao.close()
    return render_template("editar.html", usuario=usuario)

if __name__ == "__main__":
    app.run(debug=True)
