import jwt
from functools import wraps
from config.logging import Logger
from flask import request, jsonify
from config.environment import Environment


def auth_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            auth_header = request.headers.get('Authorization')

            if not auth_header:
                return jsonify({"error": "Token de autenticación requerido"}), 401

            parts = auth_header.split()
            if len(parts) != 2 or parts[0].lower() != 'bearer':
                return jsonify({"error": "Formato de token inválido. Usar: Bearer <token>"}), 401

            token = parts[1]
            auth_secret = Environment.AUTH_SECRET()

            try:
                payload = jwt.decode(token, auth_secret, algorithms=['HS256'])
                request.current_user = payload.get('user')
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expirado"}), 401
            except jwt.InvalidTokenError as e:
                Logger.error(f"Token inválido: {e}")
                return jsonify({"error": "Token inválido"}), 401

            return f(*args, **kwargs)
        except ValueError as e:
            error_message = str(e)
            Logger.error(error_message)
            return jsonify({"error": error_message}), 500
        except Exception as e:
            error_message = f"Error en autenticación: {e}"
            Logger.error(error_message)
            return jsonify({"error": error_message}), 500

    return decorated_function
