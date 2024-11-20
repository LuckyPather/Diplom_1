import pytest
from unittest.mock import Mock, patch

from praktikum.burger import Burger


class TestBurger:

    def test_init_bun(self):
        burger = Burger()
        assert burger.bun is None, "Инициализация класса отрабатывает неверно"

    def test_init_ingredients(self):
        burger = Burger()
        assert burger.ingredients == [], "Инициализация класса отрабатывает неверно"

    @pytest.mark.parametrize('name, price', [
        ("Фиолетовая", 18.0),
        ("Желтая", 19.0),
        ("Пурпурная", 20.0)
    ])
    def test_set_buns(self, name, price):
        burger = Burger()

        # Создаю Мок объект, имитирующий Bun
        mock_bun = Mock()
        mock_bun.name = name
        mock_bun.price = price

        # Проверяю начальное состояние
        assert burger.bun is None, "По умолчанию bun должен быть None"

        # Передаю mock_объект в метод set_buns
        burger.set_buns(mock_bun)

        # Проверка
        assert burger.bun is mock_bun and burger.bun.name == name and burger.bun.price == price

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ('Соус', 'Мазик', 15.0),
        ('Специи', 'Перец', 16.0),
        ('Овощи', 'Помидор', 17.0)
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        burger = Burger()

        # Создаю Мок объект, имитирующий Ingredient
        mock_ingredient = Mock()
        mock_ingredient.ingredient_type = ingredient_type
        mock_ingredient.name = name
        mock_ingredient.price = price

        # Проверяю начальное состояние
        assert burger.ingredients == [], "По умолчанию ingredients должен быть []"

        # Передаю mock объект в метод add_ingredient
        burger.add_ingredient(mock_ingredient)

        # Проверка
        assert (mock_ingredient in burger.ingredients
                and burger.ingredients[0].ingredient_type == ingredient_type and burger.ingredients[0].name == name and
                burger.ingredients[0].price == price)

    @pytest.mark.parametrize("index, name", [
        (0, "Перец"),
        (1, "Горчица")
    ])
    def test_remove_ingredient(self, index, name):
        burger = Burger()

        # Создаю Мок объект, имитирующий Ingredient 1
        mock_ingredient = Mock()
        mock_ingredient.ingredient_type = "Соус"
        mock_ingredient.name = "Горчица"
        mock_ingredient.price = 16.0

        # Создаю Мок объект, имитирующий Ingredient 2
        mock_ingredient_2 = Mock()
        mock_ingredient_2.ingredient_type = "Специи"
        mock_ingredient_2.name = "Перец"
        mock_ingredient_2.price = 17.0

        # Записываем объекты в параметр объекта класса Burger()
        burger.ingredients = [mock_ingredient, mock_ingredient_2]

        # Перед началом теста, убеждаемся что список содержит 2 объекта
        assert len(burger.ingredients) == 2, "Параметр объекта не содержит ожидаемого количества объектов"

        # Удаляем объект из списка
        burger.remove_ingredient(index)

        # Проверяем, что удалился именно нужный объект, проверяя параметр name у оставшегося объекта

        assert len(burger.ingredients) == 1 and burger.ingredients[0].name == name

    @pytest.mark.parametrize('index, new_index, ingredient_type', [
        (0, 1, 'Соус'),
        (1, 0, 'Специи'),
    ])
    def test_move_ingredient(self, index, new_index, ingredient_type):
        burger = Burger()

        # Создаю Мок объект, имитирующий Ingredient 1
        mock_ingredient = Mock()
        mock_ingredient.ingredient_type = "Соус"
        mock_ingredient.name = "Горчица"
        mock_ingredient.price = 16.0

        # Создаю Мок объект, имитирующий Ingredient 2
        mock_ingredient_2 = Mock()
        mock_ingredient_2.ingredient_type = "Специи"
        mock_ingredient_2.name = "Перец"
        mock_ingredient_2.price = 17.0

        # Записываем объекты в параметр объекта класса Burger()
        burger.ingredients = [mock_ingredient, mock_ingredient_2]

        # Перед началом теста убеждаемся в том, что по индексам расположены объекты верно
        assert burger.ingredients[index].ingredient_type == ingredient_type

        # Меняем индексы объектов
        burger.move_ingredient(index, new_index)

        # Проверяем порядок
        assert burger.ingredients[new_index].ingredient_type == ingredient_type

    @pytest.mark.parametrize('value_1, value_2, value_3, result', [
        (1.0, 2.0, 3.0, 7.0),
        (2.0, 3.0, 6.0, 13.0),
        (3.0, 6.0, 8.0, 20.0)
    ])
    def test_get_price(self, value_1, value_2, value_3, result):
        burger = Burger()

        # Создаю Мок имитирующий вызов метода get_price у объекта класса Bun
        bun_mock = Mock()
        bun_mock.get_price.return_value = value_1
        burger.bun = bun_mock

        # Создаю Мок имитирующий вызов метода get_price у объекта ingredient_mock класса Ingredient
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = value_2
        burger.ingredients.append(ingredient_mock)

        # Создаю Мок имитирующий вызов метода get_price у объекта ingredient_mock класса Ingredient
        ingredient_mock_2 = Mock()
        ingredient_mock_2.get_price.return_value = value_3
        burger.ingredients.append(ingredient_mock_2)

        assert burger.get_price() == result

    @pytest.mark.parametrize('bun_name, ingredient_type, ingredient_name, price', [
        ("Хлеб", "Соус", "Мазик", 150),
        ("Булка", "Приправа", "Перец", 200),
    ])
    def test_get_receipt(self, bun_name, ingredient_type, ingredient_name, price):
        burger = Burger()

        with patch.object(burger, 'get_price', return_value=price):
            # Создаю Мок, имитирующий вызов get_name у объекта класса Bun
            bun_mock = Mock()
            bun_mock.get_name.return_value = bun_name
            burger.bun = bun_mock

            # Создаю Мок, имитирующий вызов get_name, get_type у объекта класса Ingredient
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = ingredient_name
            burger.ingredients.append(ingredient_mock)

            # Выполняю тестируемый метод
            receipt = burger.get_receipt()
            print(receipt)

        expected_receipt = (f'(==== {bun_name} ====)\n= {ingredient_type.lower()} {ingredient_name} =\n(==== {bun_name} ====)\n'
                            f'\nPrice: {price}')
        print(expected_receipt)

        assert receipt == expected_receipt, "Результат неверный"
