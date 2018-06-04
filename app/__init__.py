from flask import Flask

app = Flask(__name__)

from app import routes
from .routes import appbp
app.register_blueprint(appbp)
