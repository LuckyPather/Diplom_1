import pytest

from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from tests.data import DataIngredient


@pytest.mark.parametrize("ingredient_type, name, price", [
    (ingredient_types.INGREDIENT_TYPE_SAUCE, DataIngredient.NAME[0], DataIngredient.PRICE[0]),
    (ingredient_types.INGREDIENT_TYPE_SAUCE, DataIngredient.NAME[1], DataIngredient.PRICE[1]),
    (ingredient_types.INGREDIENT_TYPE_FILLING, DataIngredient.NAME[2], DataIngredient.PRICE[2])
])
class TestIngredient:

    def test_init_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient_type == ingredient.type and name == ingredient.name and price == ingredient.price

    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.price == price, "Метод получения цены работает некорректно"

    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.name == name, "Метод получения имени работает некорректно"

    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type, "Метод получения типа работает некорректно"

