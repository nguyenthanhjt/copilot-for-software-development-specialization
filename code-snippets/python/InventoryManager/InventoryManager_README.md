# E-Commerce Inventory Management

This project provides an `InventoryManager` class for managing product inventory in an e-commerce application. It supports adding, removing, and checking stock for items, as well as listing low-stock products.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Integration with E-Commerce Systems](#integration-with-e-commerce-systems)
- [Contribution Guidelines](#contribution-guidelines)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ecommerce-inventory.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ecommerce-inventory
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Import the `InventoryManager` class and use it to manage your inventory:

```python
from InventoryManager_Refactored import InventoryManager, InventoryError

manager = InventoryManager()

# Add items
manager.add_item("laptop", 15)
manager.add_item("mouse", 50)

# Remove items
try:
    manager.remove_item("mouse", 5)
except InventoryError as e:
    print(e)

# Check stock
print(manager.check_stock("laptop"))  # Output: 15

# List low stock items
print(manager.list_low_stock_items())
```

---

## API Documentation

### InventoryManager

#### Methods

- **add_item(item_id: str, quantity: int) -> None**
  - Adds a specified quantity of an item to the inventory.
  - Raises `ValueError` if parameters are invalid.

- **remove_item(item_id: str, quantity: int) -> None**
  - Removes a specified quantity of an item from the inventory.
  - Raises `ValueError` if parameters are invalid.
  - Raises `InventoryError` if the item does not exist or insufficient stock.

- **check_stock(item_id: str) -> int**
  - Returns the current stock level for a given item.
  - Raises `ValueError` if `item_id` is invalid.

- **list_low_stock_items() -> List[str]**
  - Returns a list of item IDs with stock less than 5.

See [InventoryManager_Docs.md](./InventoryManager_Docs.md) for detailed documentation.

---

## Integration with E-Commerce Systems

The `InventoryManager` class can be integrated into a larger e-commerce system as the core inventory component. Typical integration points include:

- **Order Processing:** Deduct stock when orders are placed and restore stock on cancellations.
- **Product Management:** Update inventory when new products are added or restocked.
- **Admin Dashboard:** Display low-stock alerts using `list_low_stock_items()`.
- **API Layer:** Expose inventory operations via RESTful endpoints for frontend or third-party integrations.

**Example Integration:**

```python
# During order placement
def process_order(order):
    for item_id, qty in order.items():
        try:
            inventory_manager.remove_item(item_id, qty)
        except InventoryError as e:
            # Handle out-of-stock or missing item
            return {"error": str(e)}
    # Proceed with order fulfillment
```

---

## Contribution Guidelines

1. Fork the repository and create your branch:

    ```bash
    git checkout -b feature/your-feature
    ```

2. Make your changes and add tests where appropriate.
3. Ensure code style follows PEP 8.
4. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the MIT License.
