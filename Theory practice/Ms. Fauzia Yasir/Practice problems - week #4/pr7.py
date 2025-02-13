class Inventory:
    """
    A class to represent an inventory system.
    Attributes
    ----------
    item_details : dict
        A dictionary to store item details with item_id as the key.
    Methods
    -------
    __init__(self, item_id=None, item_name=None, stock_count=None, price=None):
        Initializes the inventory with an optional item.
    add_item(self, item_id, item_name, stock_count, price):
        Adds a new item to the inventory.
    update_item(self, item_id, item_name, stock_count, price):
        Updates the details of an existing item in the inventory.
    check_item_details(self, item_id):
        Returns the details of an item given its item_id.
    """
    def __init__(self, item_id=None, item_name=None, stock_count=None, price=None):
        self.item_details = {}
        if item_id is not None:
            self.item_details[item_id] = {
                'item_name': item_name,
                'stock_count': stock_count,
                'price': price
            }
    
    def add_item(self, item_id, item_name, stock_count, price):
        self.item_details[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }
    
    def update_item(self, item_id, item_name, stock_count, price):
        self.item_details[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }
    
    def check_item_details(self, item_id):
        return self.item_details.get(item_id, None)


inventory = Inventory()

# Adding items to the inventory
inventory.add_item(1, "Apple", 50, 0.5)
inventory.add_item(2, "Banana", 100, 0.2)
inventory.add_item(3, "Orange", 75, 0.3)

# Updating an item in the inventory
inventory.update_item(2, "Banana", 120, 0.25)

# Checking item details
def print_item_details(item_id):
    details = inventory.check_item_details(item_id)
    if details:
        print(f"Item ID: {item_id}")
        print(f"Item Name: {details['item_name']}")
        print(f"Stock Count: {details['stock_count']}")
        print(f"Price: ${details['price']:.2f}")
    else:
        print(f"Item ID {item_id} not found in inventory.")

    print()

print_item_details(1)
print_item_details(2)
print_item_details(3)
print_item_details(4)