from microservice1 import summ2, prod2
from flask import Flask, request
from app_service import AppService
import json

app = Flask(__name__)
appService = AppService()


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return appService.get_tasks()


@app.route('/api/task', methods=['POST'])
def create_task():
    request_data = request.get_json()

    task = request_data['task']
    if task == "summ":
        print(request_data['task'], request_data, summ2(request_data["x"], request_data["y"]))
    elif task == "prodd":
        print(request_data['task'], request_data, prod2(request_data["x"], request_data["y"]))
    return appService.create_task(task)


@app.route('/api/task', methods=['PUT'])
def update_task():
    request_data = request.get_json()
    return appService.update_task(request_data['task'])


@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)
