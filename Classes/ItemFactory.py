from Classes.MenuItem import MenuItem
from Classes.Pizza import Pizza
from Classes.Drink import Drink
from Classes.Side import Side
from typing import Optional, Union


class ItemFactory:
    """
    Is used to create items to be added to an Order.
    """

    def __init__(self):
        """
        Initialize an ItemFactory object.
        """

    def create_item(self, item: MenuItem, size: Optional[MenuItem] = None) -> Union[Pizza, Drink, Side, None]:
        """
        Create and return an instance of item to be stored in an order.
        :param item: The menu item to create for an order
        :param size: The size of the item to be ordered, if applicable.
        :return: An object whose type is likely a subclass of MenuItem,
        to be used in the Order class. Return None if the input does not meet
        certain criteria.
        """
        if item.get_type() == "Pizzas":
            return Pizza(item, size)
        elif item.get_type() == "Drinks":
            return Drink(item, size)
        elif item.get_type() == "Sides":
            return Side(item)
        else:
            return None
