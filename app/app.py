from flask import Flask, request, jsonify, send_from_directory, abort
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__, static_folder='.')

# MongoDB connection
client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
db = client["taskdb"]
tasks_collection = db["tasks"]

@app.route('/')
def serve_ui():
    return send_from_directory('.', 'index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find({}))
    for task in tasks:
        task['_id'] = str(task['_id'])  # Convert ObjectId to string
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    result = tasks_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)  # Convert ObjectId to string
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        abort(404, description="Task not found")
    return '', 204

@app.route('/tasks/<task_id>/done', methods=['PATCH'])
def mark_done(task_id):
    result = tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"done": True}}
    )
    if result.modified_count == 0:
        abort(404, description="Task not found")
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
