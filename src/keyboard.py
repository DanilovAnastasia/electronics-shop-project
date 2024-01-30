from src.item import Item


class MixinLog:
    _language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """
        Функция для изменения языка
        """
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity):
        """
        Инициализация дочернего класса
        """
        super().__init__(name, price, quantity)
