from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# from flask.ext.sqlalchemy import SQLAlchemy

# from sqlalchemy.sql import func

app = Flask(__name__)

DATABASE_PASSWORD='Mjv@2012'
DATABASE_PASSWORD_UPDATED = quote_plus(DATABASE_PASSWORD)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:"+DATABASE_PASSWORD_UPDATED+"@localhost:3306/fakepinterest"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "f$@sjg!=n!*2ypajvzn-e#4@jc-iuf#84gj_ywk$e%$k8x(32w"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manage = LoginManager(app)
login_manage.login_view = "homepage"

from fakepinterestapp import routes