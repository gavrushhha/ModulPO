# import pytest
# from products import *

# tests = [('milk', 50.0), ('bread', 50.0), ('cookies', 100.0)]

# def test_field():
#     milk = Product('milk', 66.8)
#     assert milk.name == 'milk'


# @pytest.mark.parametrize('name, price', tests)
# def test_field_name(name: str, price: float):
#     ex = Product(name, price)
#     assert ex.name == name


# @pytest.mark.parametrize('name, price', tests)
# def test_field_price(name: str, price: float):
#     ex = Product(name, price)
#     assert ex.price == price


# test_1 = [([Product('milk', 50.0), Product('bread', 50.0), Product('cookies', 100.0)], 'add')]

# @pytest.mark.parametrize('products, s', test_1)
# def test_add_basket(products: Product, s: str):
#     basket_1 = Basket()
#     for p in products:
#         basket_1.add(p)
#         assert s == basket_1.add(p)


# test_2 = [([Product('milk', 50.0), Product('bread', 50.0), Product('cookies', 100.0)], 'remove')]

# @pytest.mark.parametrize('products, s', test_2)
# def test_remove_basket(products: Product, s: str):
#     basket_2 = Basket()
#     for p in products:
#         basket_2.add(p)
#         assert s == basket_2.remove(p)


# test_3 = [([Product('milk', 50.0), Product('bread', 50.0), Product('cookies', 100.0)], 200.0)]

# @pytest.mark.parametrize('products, s', test_3)
# def test_sum_basket(products: Product, s: float):
#     basket_3 = Basket()
#     for p in products:
#         basket_3.add(p)
#     assert s == basket_3.count_sum()