from flask import (
    Flask,
    request,
    Response,
    jsonify,
    abort
)
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from config import db_uri

# APP CONFIG

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# IMPORTING MODELS
# NOTE: Models need SQLAlchemy() instance (here it is 'db')
# That is Why Models Are Imported Below, Instead Of Top

from models.task import Task
from models.student import Student
from models.teacher import Teacher
from models.status import Status

# SUPPORT FOR INLINE MIGRATION COMMAND

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ROUTES STARTS

@app.route('/')
def index():
    return jsonify({
        "message": "Please Make Request On Valid EndPoint"
    })


@app.route('/api', methods=['GET'])
def api_index():
    return jsonify({
        "message": "API IS ONLINE!!"
    })


if __name__ == '__main__':
    app.run()
