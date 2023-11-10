from csv import DictReader

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
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self._name = new_name[:10]
        else:
            self._name = new_name

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path) as file:
            reader = DictReader(file)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string:str):
        return int(float(string))

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
        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError(f'Нельзя сложить экземпляр {self.__class__} с другим объектом')

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self._name}'

