from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

db = SQLAlchemy()

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

from src.main.routes import main
from src.data_wallet.routes import data_wallet
from src.errors.routes import errors

app.register_blueprint(main)
app.register_blueprint(data_wallet)
app.register_blueprint(errors)
