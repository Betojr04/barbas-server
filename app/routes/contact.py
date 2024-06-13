from flask import Blueprint, request, jsonify
from app.models import Message
from app import db

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')
    
    if not name or not phone or not message:
        return jsonify({"error": "All fields are required"}), 400
    
    try:
        new_message = Message(name=name, phone=phone, message=message)
        db.session.add(new_message)
        db.session.commit()
        # Assuming send_mail is a function you have to send emails
        # send_mail(name, phone, message)
        return jsonify({"success": "Message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
