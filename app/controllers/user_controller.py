# app/controllers/user_controller.py


# user_bp = Blueprint('user', __name__)
from flask import Blueprint, request, jsonify
from app.models.user import User
from app import mongo  

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    user = User.find_by_username(username)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    phone = data.get('phone')
    
    if not username or not password or not phone:
        return jsonify({"message": "Missing required fields"}), 400
    
    existing_user = User.find_by_username(username)
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400
    
    User.create(username, password, phone)
    return jsonify({"message": "User created successfully"}), 201


@user_bp.route('/user/<username>', methods=['PUT'])
def update_user(username):
    data = request.get_json()
    new_password = data.get('password')
    new_phone = data.get('phone')

    if User.update(username, new_password, new_phone):
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

@user_bp.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
    user = User.find_by_username(username)
    if not user:
        return jsonify({"message": "User not found"}), 404

    # Delete the user from the database
    mongo.db.Users.delete_one({"username": username})

    return jsonify({"message": "User deleted successfully"}), 200