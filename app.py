from flask import (
    Flask,
    request,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import db_uri

# APP CONFIG

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# IMPORTING MODELS

from models import(
    Student,
    Teacher,
    Task,
    Status
)


# SUPPORT FOR INLINE MIGRATION COMMAND

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ROUTES STARTS

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
