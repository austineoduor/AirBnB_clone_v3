#!/usr/bin/python3
"""App file"""
from api.v1.views import app_views
from flask import abort, Flask, render_template, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv
from flasgger import Swagger
from flasgger.utils import swag_from


"""app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True"""
app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def handle_404(error):
    """ 
    404 Error
    responses:
      404:
        description: a resource was not found
    """
    response_error = {"error": "Not found"}
    return make_response(jsonify(response_error), 404)


"""app.config['SWAGGER'] = {


    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)"""

if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port)
