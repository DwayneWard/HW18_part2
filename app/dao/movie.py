from app.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        new_movie = Movie(**data)

        self.session.add(new_movie)
        self.session.commit()

    def get_one(self, mid: int):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_on_director(self, director_id):
        return self.session.qeury(Movie).filter(Movie.director_id == director_id)

    def get_all_on_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_all_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
