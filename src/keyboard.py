from src.item import Item


class MixinLog:
    """
    Класс миксин для хранения и изменению раскладки клавиатуры.
    """
    def __init__(self, language='EN'):
        """
        Создание экземпляра класса:
        language - Язык раскладки клавиатуры
        """
        self.language = language

    def change_lang(self):
        """Изменяет язык клавиатуры"""
        if self.language == 'EN':
            self.language = 'RU'
            return self
        else:
            self.language = 'EN'
            return self

    @property
    def language(self):
        """Геттер для __language"""
        return self.__language

    @language.setter
    def language(self, other_language):
        """Сеттер для __language"""
        if other_language == 'RU' or other_language == 'EN':
            self.__language = other_language
        else:
            print("AttributeError: property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(Item, MixinLog):
    """
    Класс для представления товара-клавиатура в магазине.
    """
    def __init__(self, name, price, quantity, language='EN'):
        """
        Создание экземпляра класса:
        name: Название товара.
        price: Цена за единицу товара.
        quantity: Количество товара в магазине.
        language - Язык раскладки клавиатуры
        """
        Item.__init__(self, name, price, quantity)
        MixinLog.__init__(self, language)
