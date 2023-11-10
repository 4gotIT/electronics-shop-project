from src.item import Item

class Phone(Item):
    """Класс телефон"""

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, {self.price}, {self.quantity}, {self.number_of_sim})'

