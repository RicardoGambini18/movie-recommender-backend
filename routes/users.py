from models import User
from flasgger import swag_from
from config.logging import Logger
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


@swag_from('../docs/users/get-user-by-id.yml')
@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = User.query.get(user_id)

        if user is None:
            return jsonify({"error": "Usuario no encontrado"}), 404

        return jsonify(user.to_dict())
    except Exception as e:
        error_message = f"Error al obtener usuario: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500
