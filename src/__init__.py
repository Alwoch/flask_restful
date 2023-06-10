from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api, Resource


def create_app():
    # create the extension
    db = SQLAlchemy()
    # create the app
    app = Flask(__name__)
    # configure the SQLite database relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    #initialize the app with the extension
    db.init_app(app)

    #import the models
    from .models.user import User

    #create the tables in the database
    with app.app_context():
        db.create_all()

    return app
