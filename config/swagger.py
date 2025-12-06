from flasgger import Swagger
from config.logger import Logger
from config.constants import is_gunicorn, port, app_name, app_description, app_version


template = {
    "swagger": "2.0",
    "basePath": "/api",
    "produces": ["application/json"],
    "consumes": ["application/json"],
    "info": {
        "title": app_name,
        "version": app_version,
        "description": app_description,
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
