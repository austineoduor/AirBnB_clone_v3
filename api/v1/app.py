#!/usr/bin/python3
"""App file"""
from api.v1.views import app_views
from flask import abort, Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
# instance of flask

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
# Initialze cross-origin

host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5000)
# Environment variables

app.register_blueprint(app_views)
# register blueprint

@app.teardown_appcontext
def teardown(exception):
    """ calls """
    storage.close()


@app.errorhandler(404)
def handle_404(error):
     """ 404 Error
    responses:
      404:
        description: a resource was not found
    """
    response_error = {"error": "Not found"}
    return make_response(jsonify(response_error), 404)


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
