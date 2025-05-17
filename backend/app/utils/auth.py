# app/utils/auth.py

from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models import User

def role_required(required_role):
    """
    Decorator to protect routes so only users with the required_role can access.
    Usage:
    @role_required('admin')
    def admin_only_route():
        ...
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()  # Ensure JWT is present and valid
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            if not user or user.role != required_role:
                return jsonify({"msg": "Access forbidden: insufficient permissions"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
