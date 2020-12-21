from Classes.MenuItem import MenuItem
from typing import List, Optional

MENU_GREETING_MSG = "Here is our menu:\n"
NO_MENU_MSG = "Sorry! It appears that our menu is empty.\n" \
              "Please check back later."


class Menu:
    """
    A menu for the pizza parlour.

    === Private Attributes ===
    _menu_items: A list of MenuItem objects stored in the Menu. It represents
    all the items being sold at this establishment (some may not be directly
    sellable like toppings).
    """
    _menu_items: List[MenuItem]

    def __init__(self):
        """
        Initializes a Menu object.
        """
        self._menu_items = []

    def __str__(self):
        """
        Return the information stored in this Menu object in a string.
        :return: The string form of this Menu object.
        """
        ret = NO_MENU_MSG
        if len(self._menu_items) != 0:
            ret = MENU_GREETING_MSG
            current_type = self._menu_items[0].get_type()
            ret += current_type + ":\n"
            for item in self._menu_items:
                if item.get_type() != current_type:
                    current_type = item.get_type()
                    ret += current_type + ":\n"
                ret += "\t" + item.__str__()
        return ret

    def add_item(self, item: MenuItem):
        """
        Adds an item to the menu.
        :param item: MenuItem object to be added.
        """
        if item not in self._menu_items:
            self._menu_items.append(item)

    def get_item(self, item_name: str, item_type: str) -> Optional[MenuItem]:
        """
        Finds and returns information about the item with name name if it exists
        in this Menu. Return None otherwise.
        :param item_name: The name of the item to find.
        :param item_type: The type of the item to find.
        :return: The item itself if it is in the Menu object. None otherwise.
        """
        for item in self._menu_items:
            if item_name == item.get_name() and item_type == item.get_type():
                return item
        return None

    def get_names(self, item_type) -> list:
        """
        Return the names of all the MenuItems with type item_type in the Menu.
        :param item_type: type of item.
        :return: All MenuItem instances with type item_type.
        """
        types = []
        for item in self._menu_items:
            if item.get_type() == item_type:
                name = item.get_name()
                if name not in types:
                    types.append(item.get_name())
        return types
