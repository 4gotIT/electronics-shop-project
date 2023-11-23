from src.item import Item

class Mixin:
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
        self.__language = language

    @property
    def language(self):
        return self.__language

    def __repr__(self):
        return f'{self.__class__.__name__} {self.price}, {self.quantity}, {self.__language}'



if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

    # kb.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter
