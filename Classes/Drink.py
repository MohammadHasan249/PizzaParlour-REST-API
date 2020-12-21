from Classes.MenuItem import MenuItem, AMOUNT
from Classes.Pizza import SIZE_UPGRADE
ICE = "ice"


class Drink(MenuItem):
    """
    A drink this Pizza Parlour serves.

    === Private Attributes ===
    _ice: Whether or not these drinks should have ice.
    _size_upgrade: The size upgrade applied on this type of drink.
    """
    _ice: bool
    _size_upgrade: MenuItem

    def __init__(self, item, size):
        """
        Initialize a Drink object.
        :param item: The item to be ordered.
        :param size: The size of the drink.
        """
        super().__init__(item.get_name(), item.get_type(), item.get_sellable(),
                         item.get_price(), item.get_amount())
        self._ice = True
        self._size_upgrade = size

    def __eq__(self, other):
        """
        Compares self and other to see if they are equal to each other.
        :param other: The Drink object to compare to self.
        :return: True if they are equal to each other, False otherwise.
        """
        return super().__eq__(other) and self._size_upgrade == \
               other.get_size() and self._ice == other.get_ice()

    def __str__(self):
        """
        Used when self is passed into print() method.
        :return: A string representative of the information in this Drink.
        """
        size_upgrade = " " + self._size_upgrade.get_name() + " "
        ret = "($%.2f) " % self.get_price() + str(self.get_amount()) + \
              size_upgrade + self.get_name() + " drink(s)"
        ice = " with no ice.\n"
        if self._ice:
            ice = " with ice.\n"
        return ret + ice

    # Setter methods

    def set_ice(self, ice):
        """
        Set whether or not ice should be added.
        :param ice: shows whether or not ice should be added.
        """
        self._ice = ice

    def set_size(self, size):
        """
        Set the size upgrade of this drink.
        :param size: The size upgrade to be applied. It is assumed to be a valid
        size upgrade for this drink.
        """
        self._size_upgrade = size

    def set_attribute(self, attribute, value):
        """
        Manipulate an attribute of this drink depending on the arguments.
        :param attribute: represents what to manipulate.
        :param value: represents the new value of the attribute to manipulate.
        """
        if attribute == AMOUNT:
            super().set_attribute(attribute, value)
        elif attribute == ICE:
            self.set_ice(value)
        elif attribute == SIZE_UPGRADE:
            self.set_size(value)

    # Getter methods

    def get_price(self):
        """
        Return the price of ordering this drink.
        :return: The total price of this drink.
        """
        base_price = super().get_price()
        size_price = self._size_upgrade.get_price()
        price_per_pizza = base_price + size_price
        return price_per_pizza * self.get_amount()

    def get_ice(self):
        """
        Return whether or not this drink has ice in it.
        :return: self._ice
        """
        return self._ice

    def get_size(self):
        """
        Return the size of this drink.
        :return: self._size_upgrade
        """
        return self._size_upgrade

    def get_attributes(self):
        """
        Return all changeable attributes for a particular item being ordered.
        :return: A list containing the names of all attributes that can be
        manipulated when placing an order.
        """
        return [AMOUNT, ICE, SIZE_UPGRADE]

