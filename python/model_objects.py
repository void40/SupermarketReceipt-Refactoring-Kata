from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, unit_price: float):
        self.name = name
        self.unit_price = unit_price


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, quantity: float, unit_price: float) -> float:
        pass


class StandardPricing(PricingStrategy):
    def calculate_price(self, quantity: float, unit_price: float) -> float:
        return quantity * unit_price


class BulkDiscountPricing(PricingStrategy):
    def __init__(self, bulk_size: int, bulk_price: float):
        self.bulk_size = bulk_size
        self.bulk_price = bulk_price

    def calculate_price(self, quantity: float, unit_price: float) -> float:
        bulk_count = quantity // self.bulk_size
        remainder = quantity % self.bulk_size
        return (bulk_count * self.bulk_price) + (remainder * unit_price)


class BuyXGetYFreePricing(PricingStrategy):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def calculate_price(self, quantity: float, unit_price: float) -> float:
        eligible_units = (quantity // (self.x + self.y)) * self.x
        remaining_units = quantity % (self.x + self.y)
        return (eligible_units + remaining_units) * unit_price
