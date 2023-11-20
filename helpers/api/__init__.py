from flask import Blueprint
from flask_restful import Api

from resources.Index import IndexResource
from resources.User import UserResource

# Api e Blueprint
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(UserResource, '/users')