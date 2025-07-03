from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
db = client["taskdb"]
tasks_collection = db["tasks"]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task['_id'] = str(task['_id'])
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    result = tasks_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
