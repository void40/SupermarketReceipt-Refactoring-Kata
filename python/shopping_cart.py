from typing import Dict


class ShoppingCart:
    def __init__(self):
        self.items: Dict[str, float] = {}

    def add_item(self, product_name: str, quantity: float):
        if product_name in self.items:
            self.items[product_name] += quantity
        else:
            self.items[product_name] = quantity

    def get_items(self) -> Dict[str, float]:
        return self.items
