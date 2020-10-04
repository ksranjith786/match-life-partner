from flask import Flask, Blueprint
from os import environ

# Blueprints
from routes.home import home_bp
from routes.login import login_bp
from routes.register import register_bp
from routes.details.create import create_bp
from routes.details.persona import persona_bp
from routes.database.query import query_bp

from database.database import createUserDB

blueprints = (home_bp, login_bp, register_bp, create_bp, persona_bp, query_bp)

def create_app():
    app = Flask(__name__)

    get_config(app)

    create_db()

    register_blueprint(app, blueprints)

    return app
# end create_app

def get_config(app):
    app.config.from_pyfile('config.py', silent=True)

    envFLASK = environ.get('FLASK_ENV')
    if envFLASK == "development":
        app.debug = True
    else:
        app.debug = False
# end get_config

def create_db():
    databaseURL = environ.get('DATABASE_URL')
    createUserDB(databaseURL)
# end create_db

def register_blueprint(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Configure explicit URL routes to home blueprint
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/home', endpoint='home')
# end register_blueprint

if __name__ == "__main__":
    app = create_app()
    app.run()
# end main
