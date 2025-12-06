from flask import Flask
from config.logger import Logger
from config.constants import debug
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from config.environment import Environment


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def setup_db(app: Flask):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = debug
    app.config["SQLALCHEMY_DATABASE_URI"] = Environment.DATABASE_URI()

    db.init_app(app)
    Logger.success('Base de datos configurada correctamente')
