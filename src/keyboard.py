from src.item import Item


class MixinLog:
    _language = 'EN'

    @property
    def language(self):
        return self._language

    # @language.setter
    # def language(self, language):
    #     self._language = language

    def change_lang(self):
        """
        Функция для изменения языка
        """
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity, language='EN'):
        """
        Инициализация дочернего класса
        """
        super().__init__(name, price, quantity)
        self._language = language