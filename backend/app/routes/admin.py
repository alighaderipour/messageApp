from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.utils.auth import role_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/users", methods=["GET"])
@role_required("admin")
def list_users():
    users = User.query.all()
    return jsonify([{ "id": u.id, "username": u.username, "email": u.email, "role": u.role } for u in users])

@admin_bp.route("/users", methods=["POST"])
@role_required("admin")
def create_user():
    data = request.json
    user = User(username=data["username"], email=data["email"], role=data["role"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@admin_bp.route("/users/<int:user_id>", methods=["PUT"])
@role_required("admin")
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.role = data.get("role", user.role)
    db.session.commit()
    return jsonify({"msg": "User updated"})

@admin_bp.route("/users/<int:user_id>", methods=["DELETE"])
@role_required("admin")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "User deleted"})