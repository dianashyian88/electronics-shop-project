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
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all += [self]

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}({str(self)}, {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию об объекте класса для пользователей"""
        return f"{self.name}"

    @property
    def name(self):
        """Геттер для __name"""
        return self.__name

    @name.setter
    def name(self, name_string):
        """Сеттер для __name"""
        if len(name_string) <= 20:
            self.__name = name_string
        else:
            print("Exception: Длина наименования товара превышает 20 символов.")

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
    def instantiate_from_csv(cls, name_file='items.csv'):
        """Инициализируюет экземпляры класса `Item` данными из файла _src/items.csv_"""
        class_file = inspect.getfile(cls)  # узнаем название файла содержащего класс
        path_to_dir = os.path.dirname(class_file)  # ищем абсолютный путь до файла
        try:
            with open(f'{path_to_dir}/{name_file}', encoding='pt154') as csvfile:
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
        except FileNotFoundError:
            print(f'Отсутствует файл {name_file}')
        except InstantiateCSVError:
            print(f'Файл {name_file} поврежден.')

    @staticmethod
    def string_to_number(string):
        """Возвращает число из числа-строки"""
        if '.' in string:
            number = string.split('.')
            return int(number[0])
        else:
            number = int(string)
            return number

    def __add__(self, other):
        """Складывает количество товаров"""
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            print('Недопустимый для сложения объект')


class InstantiateCSVError(Exception):
    """Класс исключения в случае, если файл items_1.csv поврежден"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл поврежден.'

    def __str__(self):
        return self.message
