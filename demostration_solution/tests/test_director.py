from unittest.mock import MagicMock

import pytest as pytest

from dao.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    one = Director(id=1, name="Ричард Гир")
    two = Director(id=2, name="Стивен Спилберг")
    three = Director(id=3, name="Андрей Михалков")

    director_dao.get_one = MagicMock(return_value=one)
    director_dao.get_all = MagicMock(return_value=[one, two, three])
    director_dao.create = MagicMock(return_value=one)
    director_dao.delete = MagicMock(return_value=three)
    director_dao.update = MagicMock(return_value=two)
    return director_dao

class TestGenreService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        """
        Метод создаёт объект класса DirectorService
        :param genre_dao: объект класса DirectorDAO
        """
        self.director_service = DirectorService(dao=director_dao)

    def test_get_all(self, director_dao):
        """
        Метод тестирует весь список объектов класса Director

        """
        directores = self.director_service.get_all()

        assert len(directores) > 0

    def test_get_one(self):
        """
        Метод тестирует получение одного объекта класса Director

        """
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1
        assert director.id is not None

    def test_create(self):
        """
        Метод тестирует созданный один объект класса Director
        :return:
        """
        director_d = {"name": "Джейн Камерон"}

        director = self.director_service.create(director_d)

        assert director_d is not None

    def test_update(self):
        """
        Метод тестирует добавленный объект класса Director
        """
        director_d = {"id": 1, "name": "Алексей Михалковский"}

        assert self.director_service.update(director_d) is not None
