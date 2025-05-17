from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    # Validate request has JSON data
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    data = request.get_json()
    
    # Validate required fields
    if 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400
    
    # Find user
    user = User.query.filter_by(username=data["username"]).first()
    
    # Verify user and password
    if not user or not user.check_password(data["password"]):
        return jsonify({"msg": "Bad username or password"}), 401
    
    # Create tokens
    access_token = create_access_token(
        identity=user.id,
        additional_claims={"role": user.role},
        expires_delta=timedelta(minutes=15)
    )
    refresh_token = create_refresh_token(
        identity=user.id,
        expires_delta=timedelta(days=7)
    )
    
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user_id": user.id,
        "role": user.role
    }), 200

@auth_bp.route("/api/refresh", methods=["POST"])
def refresh():
    # Implementation for token refresh would go here
    pass