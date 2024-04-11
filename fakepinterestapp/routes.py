# CRIA ROTAS DO SITE
from flask import render_template, url_for, redirect
from fakepinterestapp import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterestapp.forms import FormSignIn, FormSignUp
from fakepinterestapp.models import User, Post


@app.route("/", methods=['GET', 'POST'])
def homepage():
    formsignin = FormSignIn()
    if formsignin.validate_on_submit():
        user = User.query.filter_by(email=formsignin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formsignin.password.data):
            login_user(user)
            return redirect(url_for("profile", username=user.username) )
    return render_template('homepage.html', form=formsignin)

@app.route("/criarconta", methods=['GET', 'POST'])
def signup():
    formsignup = FormSignUp()
    if formsignup.validate_on_submit():
        password = bcrypt.generate_password_hash(formsignup.password.data)
        user = User(
            username=formsignup.username.data,
            email=formsignup.email.data,
            password=password
        )
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("profile", username=user.username) )
    return render_template("signup.html", form=formsignup)


@app.route("/perfil/<username>")
@login_required
def profile(username):
    return render_template('perfil.html', username=username)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))