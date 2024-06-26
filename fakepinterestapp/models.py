from fakepinterestapp import database, login_manage
from datetime import datetime
from flask_login import UserMixin

# RECUPERA USUARIO LOGADO
@login_manage.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    posts = database.relationship("Post", backref="user", lazy=True)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    image = database.Column(database.String, default="default.png")
    created_at = database.Column(database.DateTime, nullable=False, default=datetime.now())
    id_user = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
