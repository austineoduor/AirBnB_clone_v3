from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def stats():
    response = {}
    checkers = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
            }
    for key, val in checkers.items():
        response[val] = storage.count(key)
    return jsonify(response)
