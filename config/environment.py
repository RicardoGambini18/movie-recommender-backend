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
    def DATABASE_URI():
        database_url = os.environ.get('DATABASE_URI')
        if not database_url:
            raise ValueError(
                'La variable de entorno DATABASE_URI no está seteada')
        return database_url

    @staticmethod
    def TMDB_API_KEY():
        return os.environ.get('TMDB_API_KEY')

    @staticmethod
    def WARMUP_ITERATIONS():
        return int(os.environ.get('WARMUP_ITERATIONS', 1000))

    @staticmethod
    def MOVIES_SORT_LIMIT():
        return int(os.environ.get('MOVIES_SORT_LIMIT', 4000))

    @staticmethod
    def AUTH_PASSWORD():
        auth_password = os.environ.get('AUTH_PASSWORD')
        if not auth_password:
            raise ValueError(
                'La variable de entorno AUTH_PASSWORD no está seteada')
        return auth_password

    @staticmethod
    def AUTH_SECRET():
        auth_secret = os.environ.get('AUTH_SECRET')
        if not auth_secret:
            raise ValueError(
                'La variable de entorno AUTH_SECRET no está seteada')
        return auth_secret

    @staticmethod
    def SQLITE_DB_GOOGLE_DRIVE_ID():
        return os.environ.get('SQLITE_DB_GOOGLE_DRIVE_ID')

    @staticmethod
    def FRONTEND_ZIP_GOOGLE_DRIVE_ID():
        return os.environ.get('FRONTEND_ZIP_GOOGLE_DRIVE_ID')
