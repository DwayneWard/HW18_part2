from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    """
    Сущность SQLAlchemy, описывающая таблицу с жанарми
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
    Объект пакета marshmallow
    Схема для сериализации/десериализации данных о жанрах
    """
    id = fields.Int()
    name = fields.String()
