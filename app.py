from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config) -> Flask:
    """
    Функция реализует создание Flask приложения
    :param config: Конфигурация из файла config.py
    :return: Объект-приложение Flask
    """
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    configure_app(application)

    return application


def configure_app(application: Flask) -> None:
    """
    Функция производит настройку базы данных и Api для Flask приложения
    :param application: Объект-приложение Flask
    :return: None
    """
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app_config = Config()
app = create_app(app_config)


if __name__ == '__main__':
    app.run()
