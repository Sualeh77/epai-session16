# epai-session16
This repo is for handling the dictionary operations dynamically

# Inventory Management System

This project implements a simple inventory management system using Python. It allows users to create, update, merge, and view items in an inventory, as well as check stock levels and find the most expensive items.

## Features

- **Create Inventory**: Initialize an inventory with predefined categories and items.
- **Update Inventory**: Modify item details such as price and quantity.
- **Merge Inventories**: Combine two inventories without losing any data.
- **Retrieve Items**: Get items in a specific category or view all items.
- **Find Most Expensive Item**: Identify the most expensive item in the inventory.
- **Check Item Stock**: Verify if an item is in stock and retrieve its details.
- **View Categories**: List all available categories in the inventory.
- **Copy Inventory**: Create a deep or shallow copy of the inventory.

## Installation

To use this inventory management system, clone the repository and navigate to the project directory:

```bash
bash
git clone <repository-url>
cd <project-directory>
```


## Usage

### Creating an Inventory

You can create an inventory using the `create_inventory` function:

```python
python
from inventory_system import create_inventory
inventory = create_inventory()
```

### Updating an Item

To update an item's details, use the `update_inventory` function:
```python
python
update_info = {'price': 1200, 'quantity': 7}
update_inventory(inventory, 'Electronics', 'Laptop', update_info)
```

### Viewing Items

To view all items or items in a specific category, use:
```python
python
all_items = view_all_items(inventory)
electronics = get_items_in_category(inventory, 'Electronics')
```

### Finding the Most Expensive Item

To find the most expensive item in the inventory:
```python
python
most_expensive = find_most_expensive_item(inventory)
```

### Checking Item Stock

To check if an item is in stock:
```python
python
item_details = check_item_in_stock(inventory, 'Laptop')
```

### Viewing Categories

To view all available categories:
```python
python
categories = view_categories(inventory)
```

### Copying Inventory

To create a copy of the inventory:
```python
python
from inventory_system import copy_inventory
inventory_copy = copy_inventory(inventory, deep=True) # Deep copy
```

## Testing

This project includes unit tests to ensure the functionality of the inventory system. To run the tests, use the following command:
```bash
bash
python -m unittest test_cases.py
```

# Summary
This README provides a comprehensive overview of the inventory management system, including its features, usage instructions, and testing guidelines. You can customize it further based on specific project requirements or additional features you may want to include.