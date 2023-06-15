from src.item import Item


class Phone(Item):
    """
    Класс для представления товаров-телефонов в магазине.
    """

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}({str(self)}, {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Геттер для number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_card):
        """Сеттер для __name"""
        if count_card > 0 and isinstance(count_card, int):
            self.__number_of_sim = count_card
        else:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
