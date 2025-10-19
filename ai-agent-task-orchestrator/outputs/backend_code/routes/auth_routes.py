from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    # placeholder authentication logic
    return jsonify({"message": "Login successful", "user": data.get("username")}), 200

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}
    # placeholder signup logic
    return jsonify({"message": "Signup successful", "user": data.get("username")}), 201