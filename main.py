from init import db, ma, bcrypt, jwt 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controllers.cli_controller import db_commands


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.app_config")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)

    return app
