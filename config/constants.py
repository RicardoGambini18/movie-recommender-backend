import sys
from config.environment import Environment

app_version = "1.0.0"
app_name = "Algolab Python Server"
app_description = "Algolab es un laboratorio interactivo de algoritmos y estructuras de datos que permite experimentar con distintas implementaciones, comparar su rendimiento y visualizar su comportamiento en tiempo real, incluyendo comparadores de algoritmos de búsqueda y ordenamiento. Esta es la versión Python del servidor."

port = Environment.FLASK_RUN_PORT()
debug = Environment.FLASK_DEBUG() == "1"
mode = "Desarrollo" if debug else "Producción"

is_gunicorn = "gunicorn" in sys.argv[0]
is_flask_cli = Environment.FLASK_APP() is not None
