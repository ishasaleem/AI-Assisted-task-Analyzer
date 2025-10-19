from flask import Blueprint, request, jsonify

task_routes = Blueprint('task', __name__)

@task_routes.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return jsonify({'message': 'Task endpoint'})