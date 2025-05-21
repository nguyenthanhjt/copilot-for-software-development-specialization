from typing import Dict, List

# InventoryManager Class Documentation

## Overview

The `InventoryManager` class provides a simple interface for managing an inventory of items. It allows you to add and remove items, check stock levels, and list items that are low in stock. The class includes input validation and raises custom exceptions for inventory-related errors.

## Classes

### InventoryError

A custom exception class for inventory-related errors.

---

### InventoryManager

Manages a collection of items and their quantities.

#### Attributes

- `inventory` (`Dict[str, int]`): A dictionary mapping item IDs to their current stock quantities.

#### Methods

##### `add_item(item_id: str, quantity: int) -> None`

Adds a specified quantity of an item to the inventory.

- **Parameters:**
  - `item_id` (`str`): The unique identifier for the item.
  - `quantity` (`int`): The number of items to add (must be positive).
- **Raises:**
  - `ValueError`: If `item_id` is invalid or `quantity` is not a positive integer.

---

##### `remove_item(item_id: str, quantity: int) -> None`

Removes a specified quantity of an item from the inventory.

- **Parameters:**
  - `item_id` (`str`): The unique identifier for the item.
  - `quantity` (`int`): The number of items to remove (must be positive).
- **Raises:**
  - `ValueError`: If `item_id` is invalid or `quantity` is not a positive integer.
  - `InventoryError`: If the item does not exist or there is insufficient stock.

---

##### `check_stock(item_id: str) -> int`

Returns the current stock level for a given item.

- **Parameters:**
  - `item_id` (`str`): The unique identifier for the item.
- **Returns:**
  - `int`: The current quantity in stock (0 if the item does not exist).
- **Raises:**
  - `ValueError`: If `item_id` is invalid.

---

##### `list_low_stock_items() -> List[str]`

Returns a list of item IDs with stock less than 5.

- **Returns:**
  - `List[str]`: List of item IDs with stock below the threshold.

---

## Usage Example

```python
from RefactoredInventoryManager import InventoryManager, InventoryError

manager = InventoryManager()

# Add items
manager.add_item("apple", 10)
manager.add_item("banana", 3)

# Remove items
try:
    manager.remove_item("banana", 2)
except InventoryError as e:
    print(e)

# Check stock
print(manager.check_stock("apple"))  # Output: 10

# List low stock items
print(manager.list_low_stock_items())  # Output: ['banana']
```
