from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def create(self, data):
        return self.dao.create(data)

    def get_one(self, mid: int):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_all_on_director(self, director_id):
        return self.dao.get_all_on_director(director_id)

    def get_all_on_genre(self, genre_id):
        return self.dao.get_all_on_genre(genre_id)

    def get_all_by_year(self, year):
        return self.dao.get_all_by_year(year)

    def update(self, mid, data):
        movie = self.get_one(mid)

        movie.id = data.get('id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, mid):
        movie = self.get_one(mid)

        self.dao.delete(movie)
