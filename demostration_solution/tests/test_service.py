from unittest.mock import MagicMock

import pytest as pytest

from dao.model.movie import Movie
from dao.genre import Genre
from dao.director import Director
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    first_movie = Movie(id=1, title="Москва слезам не верит", description="О любви", trailer="www.youtube.com/watch&",
                        year=2019, rating=5, genre_id=4, director_id=1)
    second_movie = Movie(id=2, title="Титаник", description="О любви", trailer="www.youtube.com/watch?v",  year=2021, rating=7, genre_id=4, director_id=1)

    third_movie = Movie(id=3, title="Шпион", description="О шпионе", trailer="www.youtube.com/watch?v",  year=2022, rating=8, genre_id=4, director_id=1)

    movie_dao.get_one = MagicMock(return_value=first_movie)
    movie_dao.get_all = MagicMock(return_value=[first_movie, second_movie, third_movie])
    movie_dao.create = MagicMock(return_value=first_movie)
    movie_dao.update = MagicMock(return_value=second_movie)
    movie_dao.delete = MagicMock(return_value=third_movie)
    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all_movies(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0
        for movie in movies:
            assert isinstance(movie, Movie) # проверяем модель экземляра является экземляром класса Movie

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1
        assert movie.id is not None

    def test_create(self):
        movie_d = {"name": "Ужасы"}

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_update(self):
        movie_d = {"name": "Комедия"}

        assert self.movie_service.update(movie_d) is not None
