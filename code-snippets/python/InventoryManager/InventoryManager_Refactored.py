from typing import Dict, List

class InventoryError(Exception):
    """Custom exception for inventory-related errors."""
    pass

class InventoryManager:
    def __init__(self):
        """
        Initialize a new InventoryManager with an empty inventory.
        """
        self.inventory: Dict[str, int] = {}

    def add_item(self, item_id: str, quantity: int) -> None:
        """
        Add a specified quantity of an item to the inventory.

        Args:
            item_id (str): The unique identifier for the item.
            quantity (int): The number of items to add.

        Raises:
            ValueError: If item_id is invalid or quantity is not a positive integer.
        """
        self._validate_item_id(item_id)
        self._validate_quantity(quantity)
        self.inventory[item_id] = self.inventory.get(item_id, 0) + quantity

    def remove_item(self, item_id: str, quantity: int) -> None:
        """
        Remove a specified quantity of an item from the inventory.

        Args:
            item_id (str): The unique identifier for the item.
            quantity (int): The number of items to remove.

        Raises:
            ValueError: If item_id is invalid or quantity is not a positive integer.
            InventoryError: If the item does not exist or there is insufficient stock.
        """
        self._validate_item_id(item_id)
        self._validate_quantity(quantity)
        if item_id not in self.inventory:
            raise InventoryError(f"Item '{item_id}' not found in inventory.")
        if self.inventory[item_id] < quantity:
            raise InventoryError(f"Not enough items in stock for '{item_id}'.")
        self.inventory[item_id] -= quantity
        if self.inventory[item_id] == 0:
            del self.inventory[item_id]

    def check_stock(self, item_id: str) -> int:
        """
        Return the current stock level for a given item.

        Args:
            item_id (str): The unique identifier for the item.

        Returns:
            int: The current quantity in stock (0 if the item does not exist).

        Raises:
            ValueError: If item_id is invalid.
        """
        self._validate_item_id(item_id)
        return self.inventory.get(item_id, 0)

    def list_low_stock_items(self) -> List[str]:
        """
        Return a list of item IDs with stock less than 5.

        Returns:
            List[str]: List of item IDs with stock below the threshold.
        """
        return [item_id for item_id, qty in self.inventory.items() if qty < 5]

    def _validate_item_id(self, item_id: str) -> None:
        """
        Validate that the item_id is a non-empty string.

        Args:
            item_id (str): The item identifier to validate.

        Raises:
            ValueError: If item_id is not a non-empty string.
        """
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("item_id must be a non-empty string.")

    def _validate_quantity(self, quantity: int) -> None:
        """
        Validate that the quantity is a positive integer.

        Args:
            quantity (int): The quantity to validate.

        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("quantity must be a positive integer.")