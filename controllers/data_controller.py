from flask import jsonify, request
from models import data
from bson import ObjectId
from . import data_bp

@data_bp.route("/")
def hello():
    return "Hello World!"

@data_bp.route("/data", methods=["GET"])
def get_data():
    data_list = data.get_all_data()
    return jsonify(data_list)

@data_bp.route("/data", methods=["POST"])
def add_data():
    data_obj = request.json
    result = data.add_data(data_obj)
    return jsonify(str(result.inserted_id))

@data_bp.route("/data/<id>", methods=["GET"])
def get_data_by_id(id):
    document = data.get_data_by_id(id)
    return jsonify(document)

@data_bp.route("/data/<id>", methods=["PUT"])
def update_data_by_id(id):
    data_obj = request.json
    result = data.update_data_by_id(id, data_obj)
    return jsonify(str(result.modified_count))

@data_bp.route("/data/<id>", methods=["DELETE"])
def delete_data_by_id(id):
    result = data.delete_data_by_id(id)
    return jsonify(str(result.deleted_count))
