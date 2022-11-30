
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import funcs


app = Flask(__name__)
app.secret_key = 'super secret key'
# Conexão ao banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306 #Caso a porta seja a padrão, comentar linha.
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mcs2809'
app.config['MYSQL_DB'] = 'desafioweb'

mysql = MySQL(app)

@app.route("/") 
def home(): 
    return render_template("home.html")

@app.route("/quemSomos") 
def quemSomos(): 
    return render_template("quem-somos.html")

@app.route("/contato") 
def contato(mensagem = ''): 
    return render_template("contato.html", mensagem=mensagem)

@app.route("/gravarContato", methods = ['POST', 'GET'])
def gravarContato():
    if request.method == 'POST':
        descricao = request.form['descricao']
        assunto = request.form['assunto']
        email = request.form['email']
        cadastrarContato(email=email, descricao=descricao, assunto=assunto)
        return contato(mensagem='Cadastrado com sucesso!')

def cadastrarContato(email,assunto,descricao):
    cursor = mysql.connection.cursor()
    textoSQL = f"INSERT INTO contato(email, descricao, assunto) VALUES('{email}','{assunto}','{descricao}')"
    cursor.execute(textoSQL)
    mysql.connection.commit()
    cursor.close()


if __name__ == "__main__":
    app.run(debug=True)