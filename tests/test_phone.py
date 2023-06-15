"""Здесь надо написать тесты с использованием pytest для модуля phone."""
from src.item import Item
from src.phone import Phone


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'

def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == 'Phone(iPhone 14, 120000, 5, 2)'

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 4
    assert phone1.number_of_sim == 4
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == 4

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + 5 == None
    assert phone1 + 2 == None
