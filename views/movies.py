from flask import request
from flask_restx import Namespace, Resource

from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Class-Based View для отображения фильмов.
    Реализовано:
    - отображение всех фильмов GET-запросом на /movies;
    - отображение фильмов отфильтрованных по конкретному режиссеру
    (GET-запросом на /movies с использованием квери-параметра director_id);
    - отображение фильмов отфильтрованных по конкретному жанру
    (GET-запросом на /movies с использованием квери-параметра genre_id);
    - отображение фильмов отфильтрованных по конкретному году выпуска
    (GET-запросом на /movies с использованием квери-параметра year);
    - добавление нового фильма в базу данных POST-запросом на /movies.
    """

    def get(self) -> tuple:
        """
        Метод реализует отправку GET-запросов на /movies.
        Возможные варианты исполнения:
        - отображение всех фильмов GET-запросом на /movies;
        - отображение фильмов отфильтрованных по конкретному режиссеру
        (GET-запросом на /movies с использованием квери-параметра director_id);
        - отображение фильмов отфильтрованных по конкретному жанру
        (GET-запросом на /movies с использованием квери-параметра genre_id);
        - отображение фильмов отфильтрованных по конкретному году выпуска
        (GET-запросом на /movies с использованием квери-параметра year);
        :return: Сериализованные данные в формате JSON, в зависимости от реализации запроса и HTTP-код 200
        """
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        release_year = request.args.get('year')
        # Фильтрация по режиссеру
        if director_id:
            movies_with_director = db.session.query(Movie).filter(Movie.director_id == director_id)
            return movies_schema.dump(movies_with_director), 200
        # Фильтрация только по жанру
        elif genre_id:
            movies_with_genre = db.session.query(Movie).filter(Movie.genre_id == genre_id)
            return movies_schema.dump(movies_with_genre), 200
        # Фильтрация по году выпуска
        elif release_year:
            movies_by_year = db.session.query(Movie).filter(Movie.year == release_year)
            return movies_schema.dump(movies_by_year), 200
        # Без фильтрации
        all_movies = Movie.query.all()
        return movies_schema.dump(all_movies), 200

    def post(self) -> tuple:
        """
        Метод реализует отправку POST-запроса на /movies.
        Записывает данные о новом фильме с использованием переданных в формате JSON в теле POST-запроса.
        :return: Возвращает пустую строку и HTTP-код 201
        """
        json_data = request.json
        new_movie = Movie(**json_data)

        db.session.add(new_movie)
        db.session.commit()
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    Class-Based View для отображения конкретного фильма из БД.
    Реализовано:
    - отображение данных о конкретном фильме GET-запросом на /movies/id;
    - изменение данных о конкретном фильме в БД PUT-запросом на /movies/id;
    - удаление фильма из БД DELETE-запросом на /movies/id.
    """

    def get(self, mid: int) -> tuple:
        """
        Метод реализует GET-запрос на /movie/id.
        :param mid: id фильма, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        movie = Movie.query.get(mid)
        if not movie:
            return '', 404
        return movie_schema.dump(movie), 200

    def put(self, mid: int) -> tuple:
        """
        Метод реализует PUT-запрос на /movie/id.
        В теле запроса необходимо передать данные со всеми полями таблицы movie, для обновления данных.
        :param mid: id фильма, информацию о котором нужно заменить из БД.
        :return: Записывает в БД обновленные данные о конкретном фильме.
        Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        movie = Movie.query.get(mid)
        if not movie:
            return '', 404

        json_data = request.json
        movie.id = json_data.get('id')
        movie.title = json_data.get('title')
        movie.description = json_data.get('description')
        movie.trailer = json_data.get('trailer')
        movie.year = json_data.get('year')
        movie.rating = json_data.get('rating')
        movie.genre_id = json_data.get('genre_id')
        movie.director_id = json_data.get('director_id')

        db.session.add(movie)
        db.session.commit()
        return '', 204

    def delete(self, mid: int) -> tuple:
        """
        Метод реализует отправку DELETE-запроса на /movie/id.
        :param mid: id фильма, информацию о котором нужно удалить из БД.
        :return: Возвращает пустую строку и HTTP-код 204.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        movie = Movie.query.get(mid)
        if not movie:
            return '', 404

        db.session.delete(movie)
        db.session.commit()
        return '', 204
