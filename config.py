from constants import DB_NAME


class Config(object):
    SQLALCHEMY_DATABASE_URI = DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
