from dataclasses import dataclass


class ShopItem:
    def __init__(self, item_id, name, price, has_discount: bool = False):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.has_discount = has_discount

    def __repr__(self):
        return f"ShopItem({self.item_id}, {self.name}, {self.price}, {self.has_discount})"

    def __eq__(self, other):
        if isinstance(other, ShopItem):
            return (self.item_id == other.item_id and
                    self.name == other.name and
                    self.price == other.price and
                    self.has_discount == other.has_discount)
        return False


@dataclass
class ShopItem2:
    item_id: int
    name: str
    price: float
    has_discount: bool


item = ShopItem(1, "iPhone 17", 100000.00, False)
item2 = ShopItem2(1, "iPhone 17", 100000.00, False)

print(item)
# ShopItem(1, iPhone 17, 100000.0, False)

print(item2)
# ShopItem2(item_id=1, name='iPhone 17', price=100000.0, has_discount=False)
