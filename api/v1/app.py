#!/usr/bin/python3
"""App file"""
from api.v1.views import app_views
from flask import abort, Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv

# instance of flask
app = Flask(__name__)

# Initialze cross-origin
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Environment variables
host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5000)

# register blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ calls """
    storage.close()


@app.errorhandler(404)
def handle_404(error):
    response_error = {"error": "Not found"}
    return make_response(jsonify(response_error), 404)


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
