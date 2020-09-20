from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #getting the database

    db.init_app(app)    #this initializes our app with the set database

    from .messages import main  #gets our messages route functions
    app.register_blueprint(main)    #registers our blueprint

    return app