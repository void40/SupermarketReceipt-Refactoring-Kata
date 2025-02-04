from receipt import Receipt
from shopping_cart import ShoppingCart


class Teller:
    def __init__(self, supermarket: 'Supermarket'):
        self.supermarket = supermarket

    def checkout(self, cart: ShoppingCart) -> Receipt:
        return self.supermarket.checkout(cart)
