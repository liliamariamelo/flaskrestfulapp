from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with

from helpers.api import api, api_bp
from helpers.database import db, migrate
from helpers.config import get_config

# create the app
app = Flask(__name__)

# Configurations
app.config.from_object(get_config())

# Api e Blueprint
api.init_app(app)

# Database
db.init_app(app)
migrate.init_app(app=app)

with app.app_context():
    db.create_all()

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)