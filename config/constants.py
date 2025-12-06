import sys
from config.environment import Environment

port = Environment.FLASK_RUN_PORT()
debug = Environment.FLASK_DEBUG() == "1"
mode = "Desarrollo" if debug else "Producción"

is_gunicorn = "gunicorn" in sys.argv[0]
is_flask_cli = Environment.FLASK_APP() is not None
