from marshmallow import Schema, fields
from setup_db import db


class Movie(db.Model):
    """
    Сущность SQLAlchemy, описывающая таблицу с фильмами
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    Объект пакета marshmallow
    Схема для сериализации/десериализации данных о фильмах
    """
    id = fields.Int()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class Director(db.Model):
    """
    Сущность SQLAlchemy, описывающая таблицу с режиссерами
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    Объект пакета marshmallow
    Схема для сериализации/десериализации данных о режиссерах
    """
    id = fields.Int()
    name = fields.String()


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
