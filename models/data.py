from . import db
from bson import ObjectId

collection = db["students"]

def get_all_data():
    data_list = []
    for document in collection.find():
        document["_id"] = str(document["_id"])
        data_list.append(document)
    return data_list

def add_data(data_obj):
    result = collection.insert_one(data_obj)
    return result

def get_data_by_id(id):
    document = collection.find_one({"_id": ObjectId(id)})
    document["_id"] = str(document["_id"])
    return document

def update_data_by_id(id, data_obj):
    result = collection.replace_one({"_id": ObjectId(id)}, data_obj)
    return result

def delete_data_by_id(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    return result
