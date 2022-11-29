
from flask import Flask, render_template
from flask_mysqldb import MySQL
import funcs

config = funcs.LoadConfig()

app = Flask(__name__)
app.secret_key = 'super secret key'
# Conexão ao banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = '3306' #Caso a porta seja a padrão, comentar linha.
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'desafioWEB'



app = Flask("__name__")



@app.route("/") 
def home(): 
    return render_template("home.html")

@app.route("/quemSomos") 
def quemSomos(): 
    return render_template("quem-somos.html")

@app.route("/contato") 
def contato(): 
    return render_template("contato.html")

@app.route("/gravarContato")
def gravarContato():
    return

if __name__ == "__main__":
    app.run(debug=True)