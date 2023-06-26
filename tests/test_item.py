"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
import pytest
import os
import csv
import inspect


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


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) >= 5
    item1 = Item.all[0]
    print(item1)
    assert item1.name == 'Смартфон'
    with pytest.raises(InstantiateCSVError):
        class_file = inspect.getfile(Item)
        path_to_dir = os.path.dirname(class_file)
        with open(f'{path_to_dir}/items_1.csv', encoding='pt154') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if len(row) < 3:
                    raise InstantiateCSVError
                else:
                    __name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    Item.all += [row]
                    print(__name, price, quantity)
    with pytest.raises(FileNotFoundError):
        class_file = inspect.getfile(Item)
        path_to_dir = os.path.dirname(class_file)
        with open(f'{path_to_dir}/item.csv', encoding='pt154') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if len(row) < 3:
                    raise InstantiateCSVError
                else:
                    __name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    Item.all += [row]
                    print(__name, price, quantity)


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == 'Item(Смартфон, 10000, 20)'


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'
