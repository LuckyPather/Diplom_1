from unittest.mock import Mock

from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        # Создаем мок для списка булочек
        mock_buns = [Mock(), Mock(), Mock()]

        # Замокаем атрибут "buns" у экземпляра Database
        db = Database()
        db.buns = mock_buns

        # Проверяем что метод возвращает список mock_buns
        result = db.available_buns()
        assert result == mock_buns

    def test_available_ingredients(self):
        # Создаем мок для списка ингредиентов
        mock_ingredients = [Mock(), Mock(), Mock()]

        # Замокаем атрибут "ingredients" у экземпляра Database
        db = Database()
        db.ingredients = mock_ingredients

        # Проверяем что метод возвращает список mock_buns
        result = db.available_ingredients()
        assert result == mock_ingredients
