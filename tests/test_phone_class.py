from src.phone import Phone


def test_phone_class():
    test_sample1 = Phone('Samsung', 2000, 4, 3)
    test_sample2 = Phone('Смартфон', 1000, 2, 1)
    assert test_sample2.name == 'Смартфон'
    assert test_sample1 + test_sample2 == 6