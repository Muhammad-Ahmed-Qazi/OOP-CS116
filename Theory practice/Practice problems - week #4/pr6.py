class Restaurant:
    """
    A class to represent a restaurant.
    Attributes
    ----------
    menu_items : dict
        A dictionary to store menu items and their prices.
    book_table : list
        A list to store booked tables.
    customer_orders : dict
        A dictionary to store customer orders.
    Methods
    -------
    add_item_to_menu(item, price):
        Adds an item and its price to the menu.
    book_tables(table):
        Books a table.
    customer_order(customer, order):
        Adds a customer order.
    """
    def __init__(self, menu_items={}, book_table=[], customer_orders={}):
        self.menu_items = menu_items
        self.book_table = book_table
        self.customer_orders = customer_orders
    
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price
    
    def book_tables(self, table):
        self.book_table.append(table)
    
    def customer_order(self, customer, order):
        self.customer_orders[customer] = order

# Create a dummy object of Restaurant
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item_to_menu("Pasta", 12.99)
restaurant.add_item_to_menu("Pizza", 15.99)
restaurant.add_item_to_menu("Salad", 9.99)

# Make table reservations
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

# Take customer orders
restaurant.customer_order("Alice", {"Pasta": 1, "Salad": 2})
restaurant.customer_order("Bob", {"Pizza": 2})

# Print the menu
print("Menu:")
for item, price in restaurant.menu_items.items():
    print(f"{item}: ${price:.2f}")

# Print table reservations
print("\nTable Reservations:")
for table in restaurant.book_table:
    print(f"Table {table} is reserved.")

# Print customer orders
print("\nCustomer Orders:")
for customer, orders in restaurant.customer_orders.items():
    print(f"{customer} ordered:")
    for item, quantity in orders.items():
        print(f"  {quantity} x {item}")