from flask import Flask
from routes import users_bp
from flask_cors import CORS
from config import Logger, setup_db, Environment, setup_swagger

app = Flask(__name__)

CORS(app)
setup_db(app)
setup_swagger(app)

api_prefix = '/api'
app.register_blueprint(users_bp, url_prefix=api_prefix)

port = Environment.FLASK_RUN_PORT()
is_prod = Environment.FLASK_ENV() == "production"

mode = "Producción" if is_prod else "Desarrollo"
Logger.info(f"Iniciando servidor en modo {mode} en el puerto {port}")

if __name__ == "__main__":
    app.run(debug=not is_prod, port=port)
