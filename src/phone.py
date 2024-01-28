from src.item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise Exception("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        """
        Сложение экземпляров класса.
        """
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить экземпляр Phone или Item с экземпляром другого класса.")

    def __str__(self):
        """
        Возвращает название.
        """
        return self.name

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Phone.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"