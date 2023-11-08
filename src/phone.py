from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, supported_sim_cards):
        super().__init__(name, price, quantity)
        self.supported_sim_cards = supported_sim_cards

    def __add__(self, other):
        if isinstance(other, Phone):
            self.quantity += other.quantity
            return Phone(self.name, self.price, self.quantity, self.supported_sim_cards)
        raise TypeError(f'Нельзя сложить экземпляр {self.__class__} с другим об')
