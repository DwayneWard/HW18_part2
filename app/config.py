class Config:
    """
    Класс-конфигуратор приложения Flask
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db?charset=utf-8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
