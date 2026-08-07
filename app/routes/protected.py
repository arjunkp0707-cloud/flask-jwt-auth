from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

protected_bp = Blueprint("protected", __name__)


@protected_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    print("JWT DATA:", get_jwt())  # debug
    current_user = get_jwt_identity()

    return jsonify({"msg": f"Welcome {current_user}! You are authenticated"})
