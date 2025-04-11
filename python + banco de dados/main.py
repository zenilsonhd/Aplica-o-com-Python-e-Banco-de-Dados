from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para criar a tabela no banco
def criar_tabela():
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página para visualizar todos os usuários
@app.route('/usuarios')
def usuarios():
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return render_template('usuarios.html', usuarios=usuarios)

# Página de cadastro de usuário
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    return redirect(url_for('usuarios'))

# Página para buscar usuários
@app.route('/buscar', methods=['POST'])
def buscar():
    nome = request.form['nome']
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", ('%' + nome + '%',))
    usuarios = cursor.fetchall()
    conexao.close()
    return render_template('usuarios.html', usuarios=usuarios)

# Página para editar um usuário
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    if request.method == 'POST':
        novo_nome = request.form['nome']
        novo_email = request.form['email']
        cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id))
        conexao.commit()
        conexao.close()
        return redirect(url_for('usuarios'))
    else:
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        usuario = cursor.fetchone()
        conexao.close()
        return render_template('editar.html', usuario=usuario)

# Deletar usuário
@app.route('/deletar/<int:id>')
def deletar(id):
    conexao = sqlite3.connect('meubanco.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('usuarios'))

# Executar o app
if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
