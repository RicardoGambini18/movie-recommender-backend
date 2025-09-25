from models import User
from config import Logger
from flasgger import swag_from
from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__)


@swag_from('../docs/users/get-users.yml')
@users_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_data = [user.to_dict() for user in users]
        return jsonify(users_data)
    except Exception as e:
        error_message = f"Error al obtener usuarios: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500
