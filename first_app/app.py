from flask import Flask, render_template
from http import HTTPStatus
from datetime import datetime

app = Flask(__name__)

from utils.bundle import assets

@app.route('/')
def index():
	return render_template('index.jinja')

@app.route('/cours/')
def cours():
	cours = [{'Objet': 'C. Loge'}, {'Config Sys': 'C. Drocourt'}, {'BDD 1': 'C. Rottiers'}, {'Math': 'C. Masson'}]
	return render_template('cours.jinja', cours=cours)

@app.route('/hello/<string:nom>/<string:prenom>')
def fullname(nom, prenom):
	return f'Hello {prenom} {nom} comment vas tu ?', HTTPStatus.CREATED

@app.route('/ageCalculator/<int:age>')
def ageCalculator(age):
	now = datetime.now()
	return f'Naissance : 1/1/{now.year - age}', HTTPStatus.OK