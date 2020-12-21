from Classes.MenuItem import MenuItem, AMOUNT
from typing import List
TOPPINGS = "toppings"
SIZE_UPGRADE = "size upgrade"


class Pizza(MenuItem):
    """
    A pizza this Pizza Parlour serves.

    === Private Attributes ===
    _toppings: A list of toppings on this pizza.
    _size_upgrade: The size upgrade applied on this type of pizza.
    """
    _toppings: List[MenuItem]
    _size_upgrade: MenuItem

    def __init__(self, item, size):
        """
        Initialize a Pizza.
        :param item: The item to be ordered.
        :param size: The size of the pizza.
        """

        super().__init__(item.get_name(), item.get_type(), item.get_sellable,
                         item.get_price(), item.get_amount())
        self._toppings = []
        self._size_upgrade = size

    def __eq__(self, other):
        """
        Compares self and other to see if they are equal to each other.
        :param other: The Pizza object to compare to self.
        :return: True if they are equal to each other, False otherwise.
        """
        if super().__eq__(other):
            if self._size_upgrade == other.get_size() and \
                    self._check_toppings(other):
                return True
        return False

    def __str__(self):
        """
        Returns a string that accurately portrays the what this Pizza is.
        :return: A string representative of the information of this Pizza.
        """
        size_upgrade = " " + self._size_upgrade.get_name()
        ret = "($%.2f) " % self.get_price() + str(self.get_amount()) + \
              size_upgrade + " " + self.get_name() + " pizza(s)"
        toppings = " with no toppings.\n"
        if len(self._toppings):
            toppings = " with the following toppings:\n"
            for topping in self._toppings:
                toppings += "\t\t" + str(topping.get_amount()) + " " + \
                            topping.get_name() + "\n"
        return ret + toppings

    # Setter methods

    def set_topping(self, topping: MenuItem, amount: int):
        """
        Set the amount of topping in this Pizza. Remove it if this amount is 0
        or smaller.
        :param topping: The topping (MenuItem) whose amount is to be set on this
         Pizza.
        :param amount: amount of the topping.
        """
        if amount <= 0:
            if topping in self._toppings:
                self._toppings.remove(topping)
        else:
            if topping in self._toppings:
                i = self._toppings.index(topping)
                self._toppings[i].set_amount(amount)
            else:
                new_topping = MenuItem(topping.get_name(), topping.get_type(),
                                       topping.get_sellable(),
                                       topping.get_price(),
                                       amount)
                self._toppings.append(new_topping)

    def set_size(self, size: MenuItem):
        """
        Set the size upgrade of this Pizza.
        :param size: size upgrade for the Pizza.
        """
        self._size_upgrade = size

    def set_attribute(self, attribute: str, value):
        """
        Manipulate an attribute of this pizza depending on the arguments.
        :param attribute: represents what to manipulate.
        :param value: represents the new value of the attribute to manipulate.
        """
        if attribute == AMOUNT:
            super().set_attribute(attribute, value)
        elif attribute == TOPPINGS:
            for topping in value:
                self.set_topping(topping, value[topping])
        elif attribute == SIZE_UPGRADE:
            self.set_size(value)

    # Getter methods

    def get_price(self):
        """
        Calculates the total price of the Pizza(s).
        :return: Total price of this Pizza object.
        """
        base_price = super().get_price()
        size_price = self._size_upgrade.get_price()
        toppings_price = 0.0
        for topping in self._toppings:
            toppings_price += topping.get_price() * topping.get_amount()
        price_per_pizza = base_price + size_price + toppings_price
        return price_per_pizza * self.get_amount()

    def get_size(self):
        """
        Return the size upgrade of this pizza.
        :return: self._size_upgrade
        """
        return self._size_upgrade

    def get_toppings(self):
        """
        Return the list of toppings applied to this pizza.
        :return: self._toppings
        """
        return self._toppings

    def get_attributes(self):
        """
        Return all changeable attributes for a particular item being ordered.
        :return: A list containing the names of all attributes that can be
        manipulated when placing an order.
        """
        return [AMOUNT, TOPPINGS, SIZE_UPGRADE]

    # Helper method(s). Should not be called directly outside of Pizza.py

    def _check_toppings(self, other):
        """
        Checks if self and other have the same toppings in the same amounts.
        :param other: The other pizza to compare to self.
        :return: True if self and other have the same toppings in the same
        amounts. Return False otherwise.
        """
        other_toppings = other.get_toppings()
        if len(other_toppings) != len(self._toppings):
            return False
        for topping in self._toppings:
            if topping not in other_toppings:
                return False
            index = other_toppings.index(topping)
            if other_toppings[index].get_amount() != topping.get_amount():
                return False
        return True

