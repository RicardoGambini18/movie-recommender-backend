from flasgger import Swagger
from config.logger import Logger
from config.constants import is_gunicorn, port


template = {
    "swagger": "2.0",
    "basePath": "/api",
    "produces": ["application/json"],
    "consumes": ["application/json"],
    "info": {
        "version": "1.0",
        "title": "Algolab Python Server",
        "description": "Algolab es un laboratorio interactivo de algoritmos y estructuras de datos que permite experimentar con distintas implementaciones, comparar su rendimiento y visualizar su comportamiento en tiempo real, incluyendo comparadores de algoritmos de búsqueda y ordenamiento. Esta es la versión Python del servidor.",
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Token de autenticación (JWT). Formato: Bearer <token>"
        }
    },
}


def setup_swagger(app):
    if is_gunicorn:
        return

    app.config['SWAGGER'] = {
        'uiversion': 2,
        'title': 'Documentación de la API',
        'template': './resources/flasgger/swagger_ui.html'
    }

    Swagger(app, template=template)

    Logger.success(
        f"Documentación de la API configurada correctamente. Disponible en http://localhost:{port}/apidocs")
