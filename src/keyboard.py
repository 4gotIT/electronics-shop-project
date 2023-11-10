from src.item import Item

class Mixin():
    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")



class Keyboard(Item, Mixin):
    """Класс клавиатура"""
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language

    def __repr__(self):
        return f'{self.__class__.__name__} {self.price}, {self.quantity}, {self.language}'





# kb = Keyboard('Dark Project KD87A', 9600, 5)
# print(repr(kb))
# kb.change_lang()
# print(repr(kb))
