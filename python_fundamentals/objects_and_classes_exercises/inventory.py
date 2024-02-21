class Inventory:
    items = []

    def __init__(self, __capacity: int):
        self.capacity = __capacity

    def add_item(self, item: str):
        if self.capacity > len(Inventory.items):
            Inventory.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return len(Inventory.items)

    def __repr__(self):
        items = ", ".join(self.items)
        left_capacity = self.capacity - len(Inventory.items)
        return f"Items: {items}.\nCapacity left: {left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)







