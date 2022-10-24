#!/usr/bin/python3
"""App file"""
from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv

# instance of flask
app = Flask(__name__)

# Environment variables
host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5000)

# register blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ calls """
    storage.close()


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
