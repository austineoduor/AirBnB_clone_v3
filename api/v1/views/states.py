#!/usr/bin/python4
"""State views"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage, classes


@app_views.route('/states/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def states():
    if request.method == 'GET':
        lst = []
        objs = storage.all('State')
        for key, val in objs.items():
            lst.append(objs[key].to_dict())
        return jsonify(lst)

    elif request.method == 'POST':
        if not request.get_json():
            abort(400, 'Not a JSON')
        if not request.get_json("name"):
            abort(400, 'Missing name')
        State = classes.get("State")
        obj = State(request.get_json())
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'POST', 'PUT'])
def states_id(state_id):
    obj = storage.get('State', state_id)

    if request.method == 'GET':
        try:
            print(obj)
            return jsonify(obj.to_dict())
        except Exception:
            abort(404)

    if request.method == 'DELETE':
        try:
            obj.delete()
            del obj
            return jsonify({}), 200
        except Exception as e:
            return e

    if request.method == 'PUT':
        if not request.get_json():
            abort(400, 'Not a JSON')
        obj.update(request.get_json())
        return jsonify(obj.to_dict())
