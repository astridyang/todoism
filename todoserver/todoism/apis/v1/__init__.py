from flask import Blueprint, jsonify
from flask_cors import CORS

api_v1 = Blueprint('api_v1', __name__)
CORS(api_v1)


@api_v1.route('/')
def index():
    return jsonify(message="api v1 test")

from todoism.apis.v1 import resources