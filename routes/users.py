import jwt
from models import User
from flasgger import swag_from
from config.logging import Logger
from config.environment import Environment
from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta, timezone

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


@swag_from('../docs/users/login.yaml')
@users_bp.route('/users/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        user_id = data.get('user_id')
        password = data.get('password')

        if user_id is None or password is None:
            return jsonify({"error": "user_id y password son requeridos"}), 400

        user = User.query.get(user_id)
        if user is None:
            return jsonify({"error": "Usuario no encontrado"}), 404

        auth_password = Environment.AUTH_PASSWORD()
        if password != auth_password:
            return jsonify({"error": "Contraseña incorrecta"}), 400

        auth_secret = Environment.AUTH_SECRET()
        expiration = datetime.now(timezone.utc) + timedelta(days=30)

        payload = {
            'user': user.to_dict(),
            'exp': expiration
        }

        token = jwt.encode(payload, auth_secret, algorithm='HS256')

        return jsonify({"token": token})
    except ValueError as e:
        error_message = str(e)
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500
    except Exception as e:
        error_message = f"Error al iniciar sesión: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500
