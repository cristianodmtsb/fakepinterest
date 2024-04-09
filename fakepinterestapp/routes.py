# CRIA ROTAS DO SITE
from flask import render_template, url_for
from fakepinterestapp import app

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/perfil/<usuario>")
def profile(usuario):
    return render_template('perfil.html', usuario=usuario)