from Classes.MenuItem import MenuItem, AMOUNT
SAUCES = "sauces"


class Side(MenuItem):
    """
    A special side dish this Pizza Parlour serves.

    === Private Attributes ===
    _hidden_sauces: The number of special, unknown sauces in this Side dish. The
    price of one unit of this sauce is 10% of the base price of this Side dish.
    """
    _hidden_sauces = int

    def __init__(self, item):
        """
        Initialize a Side object.
        :param item: The item to be ordered.
        """
        super().__init__(item.get_name(), item.get_type(), item.get_sellable(),
                         item.get_price(), item.get_amount())
        self._hidden_sauces = 1

    def __eq__(self, other):
        """
        Compares self and other to see if they are equal to each other.
        :param other: The Side object to compare to self.
        :return: True if they are equal to each other, False otherwise.
        """
        return super().__eq__(other) and self._hidden_sauces == other.get_sauces()

    def __str__(self):
        """
        Used to when passing a Side object to print().
        :return: A string representative of the information of this Side dish.
        """
        return "($%.2f) " % self.get_price() + str(self.get_amount()) + \
               " " + self.get_name() + \
               " with " + str(self._hidden_sauces) + " sauces each.\n"

    # Setter methods

    def set_attribute(self, attribute, value):
        """
        Manipulate an attribute of this side depending on the arguments.
        :param attribute: represents what to manipulate.
        :param value: represents the new value of the attribute to manipulate.
        """
        if attribute == AMOUNT:
            super().set_attribute(attribute, value)
        elif attribute == SAUCES:
            self.set_sauces(value)

    def set_sauces(self, amount):
        """
        Set the number of side dishes of this type to be ordered.
        :param amount: number of side dishes.
        """
        self._hidden_sauces = amount

    # Getter methods

    def get_sauces(self):
        """
        Return the amount of this Side dish being ordered.
        :return: self._amount
        """
        return self._hidden_sauces

    def get_attributes(self):
        """
        Return all changeable attributes for a particular item being ordered.
        :return: A list containing the names of all attributes that can be
        manipulated when placing an order.
        """
        return [AMOUNT, SAUCES]
