from flask_restful import Resource, marshal_with
from helpers.logger import logger

from models.User import User, userFields

class UserResource(Resource):
    @marshal_with(userFields)
    def get(self):
        logger.info("Listando os Users.")
        users = User.query.all()
        return users, 200