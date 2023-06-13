import os
import csv
import inspect


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all += [self]

    @property
    def name(self):
        """Геттер для __name"""
        return self.__name

    @name.setter
    def name(self, name_string):
        """Сеттер для __name"""
        if len(name_string) <= 10:
            self.__name = name_string
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализируюет экземпляры класса `Item` данными из файла _src/items.csv_"""
        class_file = inspect.getfile(cls)  # узнаем название файла содержащего класс
        path_to_dir = os.path.dirname(class_file)  # ищем абсолютный путь до файла
        with open(f'{path_to_dir}/items.csv', encoding='pt154') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                __name = row['name']
                price = row['price']
                quantity = row['quantity']
                Item.all += [row]
                print(__name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """Возвращает число из числа-строки"""
        if '.' in string:
            number = string.split('.')
            return int(number[0])
        else:
            number = int(string)
            return number
