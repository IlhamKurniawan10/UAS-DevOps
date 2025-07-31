class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, quantity)

    def get_quantity(self, name):
        return self.items.get(name, Item(name, 0)).quantity

    def remove_item(self, name, quantity):
        if name in self.items and self.items[name].quantity >= quantity:
            self.items[name].quantity -= quantity
            return True
        return False
