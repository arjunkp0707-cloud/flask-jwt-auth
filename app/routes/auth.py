from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

# in-memory storage
users = {}


# ---------------- REGISTER ----------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password are required"}), 400

    if username in users:
        return jsonify({"msg": "user already exists"}), 400

    users[username] = generate_password_hash(password)

    return jsonify({"msg": "user registered successfully"}), 201


# ---------------- LOGIN ----------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"msg": "User not found"}), 404

    if not check_password_hash(users[username], password):
        return jsonify({"msg": "Wrong password"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token})


# ---------------- REFRESH ----------------
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()

    return jsonify(
        {
            "access_token": create_access_token(identity=identity),
            "refresh_token": create_refresh_token(identity=identity),  # rotation
        }
    )
