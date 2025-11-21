from flask import Flask
from config.logger import Logger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from config.environment import Environment


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def setup_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = Environment.DATABASE_URI()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Environment.FLASK_ENV(
    ) == "development"

    db.init_app(app)
    Logger.info('Base de datos configurada')
