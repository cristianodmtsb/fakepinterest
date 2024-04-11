from fakepinterestapp import database, app
from fakepinterestapp.models import User, Post

with app.app_context():
    database.create_all()