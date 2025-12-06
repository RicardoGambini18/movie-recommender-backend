from pathlib import Path
from flask_cors import CORS
from config.logger import Logger
from config.database import setup_db
from routes import users_bp, movies_bp
from config.swagger import setup_swagger
from flask import Flask, send_from_directory, abort
from config.constants import port, debug, mode, is_flask_cli, is_gunicorn

app = Flask(__name__)

CORS(app)
setup_db(app)
setup_swagger(app)

api_prefix = '/api'
app.register_blueprint(users_bp, url_prefix=api_prefix)
app.register_blueprint(movies_bp, url_prefix=api_prefix)

frontend_path = Path(__file__).parent / "frontend"
frontend_index = frontend_path / "index.html"
serve_frontend = frontend_index.exists()

if serve_frontend:
    Logger.info("Archivos estáticos del frontend habilitados")
    frontend_directory = str(frontend_path)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_frontend_app(path):
        if path.startswith('api/'):
            abort(404)

        requested_file = frontend_path / path
        if path and requested_file.is_file():
            return send_from_directory(frontend_directory, path)

        return send_from_directory(frontend_directory, 'index.html')


is_main = __name__ == "__main__"

if is_flask_cli or is_main:
    Logger.success(
        f"Servidor iniciado correctamente en modo {mode}. Disponible en http://localhost:{port}")
elif is_gunicorn:
    Logger.success(
        f"Servidor iniciado correctamente en modo {mode}")

if is_main:
    app.run(debug=debug, port=port)
