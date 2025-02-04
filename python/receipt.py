from typing import List


class Receipt:
    def __init__(self):
        self.items: List[str] = []
        self.total: float = 0.0

    def add_item(self, product_name: str, quantity: float, price: float):
        self.items.append(f"{product_name} x{quantity}: ${price:.2f}")
        self.total += price

    def get_items(self) -> List[str]:
        return self.items

    def get_total(self) -> float:
        return self.total
