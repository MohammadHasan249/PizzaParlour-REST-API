import os
import csv
from Classes.Delivery import Delivery

FOODORA = "Foodora"


class FoodoraDelivery(Delivery):
    """
    A delivery that Foodora has to make.

    === Private Attributes ===
    _file: The file to save the order to.
    """
    _file: str

    def __init__(self, order, file):
        """
        Initialize an UberEatsDelivery object.
        :param file: The json file to store the order in.
        """
        super().__init__(order, FOODORA)
        self._file = file

    def deliver(self):
        """
        Deliver the order.
        :return A string if the delivery was saved successfully. None otherwise.
        """
        if not self._file.endswith(".csv"):
            return None
        try:
            with open(self._file, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow("Address: " + super().get_address())
                writer.writerow("Order details: ")
                for item in super().get_order().get_cart():
                    writer.writerow("\t" + item.__str__())
                writer.writerow("Order number: " + str(super().get_order().
                                get_order_number()))
            return super().deliver()
        except IOError:
            print("IO Error")
            return None

    # Getter methods

    def get_file(self):
        """
        Return the file to storing the delivery in.
        :return: self._file
        """
        return self._file

