from csv import DictReader


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """
        Вывод имени класса, и его атрибутов
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Вывод наименования товара
        """
        return self.__name

    def __add__(self, other):
        """
        Сложение экземпляров класса.
        """
        return self.quantity + other.quantity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, str_name):
        if len(str_name) <= 10:
            self.__name = str_name
        else:
            self.__name = str_name[0:10]
            raise Exception("длина наименования товара больше 10 символов")

    @classmethod
    def instantiate_from_csv(cls, file_path):
        Item.all = []
        try:
            with open(file_path, 'r', encoding='cp1251') as csv_file:
                items = DictReader(csv_file, delimiter=',')
                for row in items:
                    if len(items.fieldnames) == 3 and len(row) == 3:
                        cls(row['name'], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError('Формат файла не соответсвует')
        except KeyError:
            raise InstantiateCSVError("Файл поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(str):
        try:
            return int(float(str))
        except ValueError:
            return "Невозможно преобразовать строку в натуральное число"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
