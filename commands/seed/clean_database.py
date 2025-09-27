from config.database import db
from config.logging import Logger


def clean_database():
    Logger.info("Limpiando base de datos")
    db.drop_all()
    db.create_all()
    Logger.success("Base de datos limpiada correctamente")
