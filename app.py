from flask import Flask
from flask_cors import CORS
from config.logging import Logger
from config.database import setup_db
from routes import users_bp, movies_bp
from config.swagger import setup_swagger
from config.environment import Environment
from config.commands import register_commands

# Se necesita importar todos los modelos para que flask-migrate los registre
from models import *

app = Flask(__name__)

CORS(app)
setup_db(app)
setup_swagger(app)
register_commands(app)

api_prefix = '/api'
app.register_blueprint(users_bp, url_prefix=api_prefix)
app.register_blueprint(movies_bp, url_prefix=api_prefix)

port = Environment.FLASK_RUN_PORT()
debug = Environment.FLASK_DEBUG() == "1"
is_prod = Environment.FLASK_ENV() == "production"

mode = "Producción" if is_prod else "Desarrollo"
debug_state = "Activado" if debug else "Desactivado"
Logger.info(
    f"Iniciando servidor en modo {mode} (Debug: {debug_state}) en el puerto {port}")

if __name__ == "__main__":
    app.run(debug=not is_prod, port=port)
