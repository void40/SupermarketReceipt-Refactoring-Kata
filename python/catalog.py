from typing import Dict

from model_objects import PricingStrategy, \
    Product, StandardPricing
from receipt import Receipt
from shopping_cart import ShoppingCart


class SupermarketCatalog:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.pricing_strategies: Dict[str, PricingStrategy] = {}

    def add_product(self, product: Product, strategy: PricingStrategy):
        self.products[product.name] = product
        self.pricing_strategies[product.name] = strategy

    def checkout(self, cart: ShoppingCart) -> Receipt:
        receipt = Receipt()
        for product_name, quantity in cart.get_items().items():
            product = self.products.get(product_name)
            strategy = self.pricing_strategies.get(product_name, StandardPricing())
            if product:
                price = strategy.calculate_price(quantity, product.unit_price)
                receipt.add_item(product_name, quantity, price)
        return receipt
