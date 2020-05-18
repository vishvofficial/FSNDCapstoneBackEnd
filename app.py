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


# CORS CONFIG

CORS(app, resources={
    r'/api/*': {
        'origins': '*'
    }
})


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type, Authorization, true'
    )
    response.headers.add(
        'Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PATCH, DELETE'
    )
    return response


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


# ERROR HANDLERS


@app.errorhandler(400)
def bad_request():
    return jsonify({
        "error_code": 400,
        "description": "A Bad Request"
    }), 400


@app.errorhandler(401)
def not_authorized():
    return jsonify({
        "error_code": 401,
        "description": "Unauthorized"
    })


@app.errorhandler(404)
def nothing_found():
    return jsonify({
        "error_code": 404,
        "description": "Resource Not Found"
    }), 404


@app.errorhandler(405)
def not_allowed():
    return jsonify({
        "error_code": 405,
        "description": "Request Method Not Allowed"
    }), 405


@app.errorhandler(500)
def not_allowed():
    return jsonify({
        "error_code": 500,
        "description": "Something Wrong Happened At Our Side\nPlease Try After Sometime"
    }), 405


if __name__ == '__main__':
    app.run()
