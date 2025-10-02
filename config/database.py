from flask import Flask
from flask_migrate import Migrate
from config.logging import Logger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from config.environment import Environment


class Base(DeclarativeBase):
    pass


migrate = Migrate()
db = SQLAlchemy(model_class=Base)


def setup_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = Environment.DATABASE_URL()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Environment.FLASK_ENV(
    ) == "development"

    db.init_app(app)
    migrate.init_app(app, db)
    Logger.info('Base de datos configurada')
