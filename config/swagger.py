from flasgger import Swagger
from config.logging import Logger


template = {
    "swagger": "2.0",
    "basePath": "/api",
    "produces": ["application/json"],
    "consumes": ["application/json"],
    "info": {
        "version": "1.0",
        "title": "API Recomendador de Películas",
        "description": "API del proyecto final del curso Estadística y Estructuras de Datos",
    },
}


def setup_swagger(app):
    app.config['SWAGGER'] = {
        'uiversion': 2,
        'title': 'Documentación de la API',
        'template': './resources/flasgger/swagger_ui.html'
    }

    Swagger(app, template=template)
    Logger.info('Documentación de la API configurada en /apidocs')
