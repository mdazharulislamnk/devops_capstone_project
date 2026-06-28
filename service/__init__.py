from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
talisman = Talisman(app, force_https=False)
CORS(app)

from service import routes, models
