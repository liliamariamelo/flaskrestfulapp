from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

# initialize the app with the extension
db = SQLAlchemy(model_class=Base)

# Migrate
migrate = Migrate(db=db)