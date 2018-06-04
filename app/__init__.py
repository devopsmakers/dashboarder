from .routes import appbp

from flask import Flask

app = Flask(__name__)
app.register_blueprint(appbp)
