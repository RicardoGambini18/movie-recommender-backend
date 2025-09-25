import os
from dotenv import load_dotenv

load_dotenv()


class Environment:
    @staticmethod
    def FLASK_ENV():
        return os.environ.get('FLASK_ENV', 'development')

    @staticmethod
    def DATABASE_URL():
        database_url = os.environ.get('DATABASE_URL')
        if not database_url:
            raise ValueError('DATABASE_URL is not set')
        return database_url

    @staticmethod
    def PORT():
        return int(os.environ.get('PORT', 8080))
