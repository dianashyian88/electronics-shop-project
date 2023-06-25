from src.item import Item

if __name__ == '__main__':
    # Файл items_1.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items_1.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
