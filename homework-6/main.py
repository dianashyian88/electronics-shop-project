from src.item import Item
import os

if __name__ == '__main__':
    # Файл items_1.csv отсутствует.
    Item.instantiate_from_csv('item.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items_1.csv удалена последняя колонка.
    Item.instantiate_from_csv('items_1.csv')
    # InstantiateCSVError: Файл items_1.csv поврежден
