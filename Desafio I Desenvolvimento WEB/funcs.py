from flask_mysqldb import MySQL
from flask import Flask, render_template,request, url_for, redirect, session, abort

app = Flask(__name__)


mysql = MySQL(app)


