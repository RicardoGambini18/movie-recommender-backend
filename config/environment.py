import os
from dotenv import load_dotenv

load_dotenv()


class Environment:
    @staticmethod
    def FLASK_DEBUG():
        return os.environ.get('FLASK_DEBUG', '0')

    @staticmethod
    def FLASK_RUN_PORT():
        return int(os.environ.get('FLASK_RUN_PORT', 5000))

    @staticmethod
    def FLASK_ENV():
        return os.environ.get('FLASK_ENV', 'development')

    @staticmethod
    def DATABASE_URL():
        database_url = os.environ.get('DATABASE_URL')
        if not database_url:
            raise ValueError(
                'La variable de entorno DATABASE_URL no está seteada')
        return database_url

    @staticmethod
    def TMDB_API_KEY():
        return os.environ.get('TMDB_API_KEY')
