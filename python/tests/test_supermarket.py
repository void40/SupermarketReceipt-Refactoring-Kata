import pytest

from catalog import SupermarketCatalog
from model_objects import Product, StandardPricing, \
    BulkDiscountPricing, BuyXGetYFreePricing
from receipt_printer import ReceiptPrinter
from shopping_cart import ShoppingCart
from teller import Teller


@pytest.fixture
def store():
    store = SupermarketCatalog()
    store.add_product(Product("Apple", 1.0), StandardPricing())
    store.add_product(Product("Banana", 0.5), BuyXGetYFreePricing(2, 1))
    store.add_product(Product("Cereal", 4.0), BulkDiscountPricing(3, 10.0))
    return store


@pytest.fixture
def cart():
    return ShoppingCart()


def test_standard_pricing(store, cart):
    cart.add_item("Apple", 5)
    teller = Teller(store)
    receipt = teller.checkout(cart)
    assert receipt.get_total() == pytest.approx(5.0)


def test_buy_x_get_y_free_pricing(store, cart):
    cart.add_item("Banana", 6)
    teller = Teller(store)
    receipt = teller.checkout(cart)
    assert receipt.get_total() == pytest.approx(2.0)  # 6 bananas, pay for 4


def test_bulk_discount_pricing(store, cart):
    cart.add_item("Cereal", 4)
    teller = Teller(store)
    receipt = teller.checkout(cart)
    assert receipt.get_total() == pytest.approx(14.0)  # 3 for $10, 1 at $4


def test_mixed_cart(store, cart):
    cart.add_item("Apple", 5)
    cart.add_item("Banana", 6)
    cart.add_item("Cereal", 4)
    teller = Teller(store)
    receipt = teller.checkout(cart)
    assert receipt.get_total() == pytest.approx(21.0)


def test_receipt_printing(store, cart, capsys):
    cart.add_item("Apple", 5)
    teller = Teller(store)
    receipt = teller.checkout(cart)
    ReceiptPrinter.print_receipt(receipt)
    captured = capsys.readouterr()
    assert "Apple x5: $5.00" in captured.out
    assert "Total: $5.00" in captured.out
