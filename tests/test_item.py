"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0


def test_item():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.name == "Смартфон"
    assert isinstance(item1.price, int)
    assert isinstance(Item.all, list)