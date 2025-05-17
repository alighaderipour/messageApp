from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Message

messages_bp = Blueprint('messages', __name__)

@messages_bp.route("/api/messages", methods=["GET"])
@jwt_required()
def get_messages():
    user_id = get_jwt_identity()
    messages = Message.query.filter_by(receiver_id=user_id).all()
    return jsonify([{
        "id": m.id,
        "sender_id": m.sender_id,
        "content": m.content,
        "timestamp": m.timestamp.isoformat()
    } for m in messages])

@messages_bp.route("/api/messages", methods=["POST"])
@jwt_required()
def send_message():
    data = request.json
    sender_id = get_jwt_identity()
    message = Message(sender_id=sender_id, receiver_id=data["receiver_id"], content=data["content"])
    db.session.add(message)
    db.session.commit()
    return jsonify({"msg": "Message sent"}), 201