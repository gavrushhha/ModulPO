from ProductandBasket import *
import pytest


test1 = [([Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)], 'add')]
@pytest.mark.parametrize('product, s', test1)
def test_add(product: Product, s: str):
    basket1 = Basket()
    for p in product:
        basket1.add(p)
        assert s == basket1.add(p)

test2 = [([Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)], 'remove')]
@pytest.mark.parametrize('product, s', test2)
def test_remove(product: Product, s: str):
    basket2 = Basket()
    for p in product:
        basket2.add(p)
    assert s == basket2.remove(p)

test3 = [([Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)], 170.0)]
@pytest.mark.parametrize('product, s', test3)
def test_summ(product: Product, s: float):
    basket3 = Basket()
    for p in product:
        basket3.add(p)
    assert s == basket3.count_sum()

test4 = [('bread', 50.0), ('carrot', 20.0)]
def test_field():
    bread = Product('bread', 50.0)
    assert bread.name == 'bread'


@pytest.mark.parametrize('name, price', test4)
def test_name(name: str, price: float):
    field_name = Product(name, price)
    assert field_name.name == name


@pytest.mark.parametrize('name, price', test4)
def test_price(name: str, price: float):
    field_price = Product(name, price)
    assert field_price.price == price




