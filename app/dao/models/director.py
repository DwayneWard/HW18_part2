from marshmallow import Schema, fields

from app.setup_db import db


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
