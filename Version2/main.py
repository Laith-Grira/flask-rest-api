from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data", methods=["GET"])
def get_data():
    data = []
    for document in collection.find():
        document["_id"] = str(document["_id"])
        data.append(document)
    return jsonify(data)

@app.route("/data", methods=["POST"])
def add_data():
    data = request.json
    result = collection.insert_one(data)
    return jsonify(str(result.inserted_id))

@app.route("/data/<id>", methods=["GET"])
def get_data_by_id(id):
    document = collection.find_one({"_id": ObjectId(id)})
    document["_id"] = str(document["_id"])
    return jsonify(document)

@app.route("/data/<id>", methods=["PUT"])
def update_data_by_id(id):
    data = request.json
    result = collection.replace_one({"_id": ObjectId(id)}, data)
    return jsonify(str(result.modified_count))

@app.route("/data/<id>", methods=["DELETE"])
def delete_data_by_id(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    return jsonify(str(result.deleted_count))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
