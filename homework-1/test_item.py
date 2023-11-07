from src.item import Item
import pytest


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

def test_item():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_change_rate():
    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000

