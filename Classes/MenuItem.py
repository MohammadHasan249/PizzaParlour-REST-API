AMOUNT = "amount"


class MenuItem:
    """
    An item that the Pizza Parlour serves.

    === Private Attributes ===
    _name: The name of the item.
    _type: The type of item it is.
    _sellable: Whether or not the item is directly sellable or not.
    _price: The price of the item (for the smallest size available).
    _amount: The amount of the item.
    """
    _name: str
    _type: str
    _sellable: bool
    _price: float
    _amount: int

    def __init__(self, item_name, item_type, sellable, item_price, amount):
        """
        Initializes a MenuItem object.
        """
        self._name = item_name
        self._type = item_type
        self._sellable = sellable
        self._price = item_price
        self._amount = amount

    def __eq__(self, other):
        """
        Checks if 2 MenuItem objects are equal to one another.
        :param other: The MenuItem object to compare to self.
        :return True if they are equal to each other and False otherwise.
        """
        check_name = self._name == other.get_name()
        check_type = self._type == other.get_type()
        check_sellable = self._sellable == other.get_sellable()
        return check_name and check_type and check_sellable

    def __str__(self):
        """
        Used when self is passed into print() method.
        :return: A string representative of the information in this MenuItem.
        """
        return self._name + ": ${:.2f}\n".format(self._price)

    def __hash__(self):
        """
        Allows MenuItems to be hashed. Useful for being a key in a dictionary.
        :return: This MenuItem object's hash value.
        """
        return hash((self._name, self._type))

    def set_amount(self, amount):
        """
        Set the number of units of an item being ordered.
        :param amount: the desired amount for the item.
        """
        self._amount = amount

    def set_attribute(self, attribute, value) -> None:
        """
        Alter the attribute attribute of this item.
        :param attribute: Attribute to change.
        :param value: The value to change the attribute to.
        """
        if attribute == AMOUNT:
            self.set_amount(value)

    # Getter methods

    def get_name(self):
        """
        :return: The name of the MenuItem.
        """
        return self._name

    def get_type(self):
        """
        :return: The type of the MenuItem.
        """
        return self._type

    def get_sellable(self):
        """
        :return: The sellable status of the MenuItem.
        """
        return self._sellable

    def get_price(self):
        """
        :return: The price of the MenuItem.
        """
        return self._price

    def get_amount(self):
        """
        Returns the number of units of an item being ordered.
        :return self._amount
        """
        return self._amount

    def get_attributes(self) -> list:
        """
        Return all changeable attributes for a particular item being ordered.
        All child classes of MenuItem must override this.
        The MenuItem class itself will not implement this.
        """
        return [AMOUNT]
