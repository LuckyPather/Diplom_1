import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', [
        ("Ядерная", 15.0),
        ("Красная", 16.0),
        ("Зеленая", 17.0)
    ])
    def test_init_name(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name, "Имя не соответсвует переданному"

    @pytest.mark.parametrize('name, price', [
        ("Фиолетовая", 18.0),
        ("Желтая", 19.0),
        ("Пурпурная", 20.0)
    ])
    def test_init_price(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price, "Цена не соответсвует переданной"

    @pytest.mark.parametrize('name, price', [
        ("Коричневая", 21.0),
        ("Черная", 22.0),
        ("Зеленая", 17.0)
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name, "Метод получения имени работает неверно"

    @pytest.mark.parametrize('name, price', [
        ("Ядерная", 15.0),
        ("Красная", 16.0),
        ("Зеленая", 17.0)
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price, "Метод получения цены работает неверно"
