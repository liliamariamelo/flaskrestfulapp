from flask_restful import fields

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from helpers.database import db

userFields = {
  'id': fields.Integer,
  'username': fields.String,
  'email': fields.String
}
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)