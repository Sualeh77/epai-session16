# inventory_system.py

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    elec_prods = ["Laptop", "Tablet"]
    keys_ = ("name", "price", "quantity")
    laptop_values = ("Laptop", 1100, 8)
    tablet_values = ("Tablet", 500, 15)
    inventory = {
        'Electronics': {
                prod: {
                    k:v for k,v in zip(keys_, laptop_values if prod=="Laptop" else tablet_values)
                } for prod in elec_prods
        },
        'Groceries': dict()
    }
    return inventory


def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    inventory[category] = {item_name : update_info}

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    return {**inv1, **inv2}


def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory.get(category)

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    most_expensive_item = None
    max_price = 0
    stack = [(inventory, "inventory")]
    while stack:
        d, item = stack.pop()
        for k, v in d.items():
            if isinstance(v, dict) and v:
                stack.append((v, k))
            else:
                if k == "price" and v > max_price:
                    most_expensive_item = {"name": item, "price": v}
                    max_price = v
    return most_expensive_item

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category in inventory:
        return inventory[category].get(item_name) if item_name in inventory[category] else None

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    all_items = []
    for category, items in inventory.items():
        for item in items.values():
            all_items.append(item)
    return all_items

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    return inventory.items()

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    from copy import deepcopy
    return deepcopy(inventory) if deep else inventory.copy()
