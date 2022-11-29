from flask_mysqldb import MySQL
from flask import Flask, render_template,request, url_for, redirect, session, abort

app = Flask(__name__)


mysql = MySQL(app)


def cadastrarContato(email,assunto,descricao):
    cursor = mysql.connection.cursor()
    textoSQL = f'INSERT INTO contato(email, descricao, assunto) VALUES({email},{assunto},{descricao})'
    cursor.execute(textoSQL)
    resultado = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
