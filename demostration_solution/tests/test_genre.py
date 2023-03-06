from unittest.mock import MagicMock

import pytest as pytest

from dao.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    one = Genre(id=1, name="Action")
    two = Genre(id=2, name="Adventure")
    three = Genre(id=3, name="Comedy")

    genre_dao.get_one = MagicMock(return_value=one)
    genre_dao.get_all = MagicMock(return_value=[one, two, three])
    genre_dao.create = MagicMock(return_value=one)
    genre_dao.delete = MagicMock(return_value=two)
    genre_dao.update = MagicMock(return_value=three)
    return genre_dao

class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        """
        Метод создаёт объект класса GenreService
        :param genre_dao: объект класса GenreDAO
        """
        self.genre_service = GenreService(dao=genre_dao)


    def test_get_all(self, genre_dao):
        """
        Метод тестирует весь список объектов класса Genre

        """
        genres = self.genre_service.get_all()

        assert len(genres) == 3
        for genre in genres:
            assert isinstance(genre, Genre)

    def test_get_one(self):
        """
        Метод тестирует получение одного объекта класса Genre

        """
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id == 1
        assert genre.id is not None

    def test_create(self):
        """
        Метод тестирует созданный один объект класса Genre
        :return:
        """
        genre_d = {"name": "Ужасы"}

        genre = self.genre_service.create(genre_d)

        assert genre_d is not None

    def test_update(self):
        """
        Метод тестирует добавленный объект класса Genre
        """
        genre_d = {"id": 1, "name": "Комедия"}

        assert self.genre_service.update(genre_d) is not None
