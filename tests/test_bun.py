import pytest

from praktikum.bun import Bun
from tests.data import DataBun


@pytest.mark.parametrize('name, price', [
    (DataBun.NAME[0], DataBun.PRICE[0]),
    (DataBun.NAME[1], DataBun.PRICE[1]),
    (DataBun.NAME[2], DataBun.PRICE[2])
])
class TestBun:

    def test_init_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name and bun.price == price, "Имя не соответствует переданному"

    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name, "Метод получения имени работает неверно"

    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price, "Метод получения цены работает неверно"
