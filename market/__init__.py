'''
__init__.py make the market folder as the library package and
can be imported as "from market import db" in run.py
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # store password as hash password
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# if is not logged in, go to login route "login_page" in routes.py
login_manager.login_view = "login_page"
# show the message in background color of blue (category of "info")
login_manager.login_message_category = "info"

# import routes
from market import routes