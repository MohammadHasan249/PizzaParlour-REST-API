from typing import Dict
from Classes import Order

DELIVERY_MADE = " will arrive shortly with your food. Thank you for your order!"


class Delivery:
    """
    A delivery that the Pizza Parlour (or any third-party delivery
    service) has to make.

    === Private Attributes ===
    _order: the order to be delivered.
    _address: the address to deliver the order to.
    _deliverer: the entity responsible for delivering this order.
    """
    _order: Order
    _address: str
    _deliverer: str

    def __init__(self, order: Order, deliverer: str) -> None:
        """
        Initializes a Delivery object.
        :param order: order to be delivered.
        :param deliverer: The name of the deliverer.
        """
        self._order = order
        self._address = ""
        self._deliverer = deliverer

    def make_dict(self) -> Dict:
        """
        Returns this Delivery in dictionary form.
        :return: The information in this object as a dictionary.
        """
        ret = {
               "Order Number": self._order.get_order_number(),
               "Address": self._address,
               "Order Details": self._order.__str__()
               }
        return ret

    def set_address(self, address: str):
        """
        Set the address to deliver the order to.
        :param address: address of the buyer.
        """
        self._address = address

    def deliver(self):
        """
        Deliver the order.
        """
        if self._address == "":
            return None
        else:
            return "A delivery driver working for " + self._deliverer + \
                   DELIVERY_MADE

    # Getter methods

    def get_order(self):
        """
        Return the order for this delivery.
        :return: self._order
        """
        return self._order

    def get_address(self):
        """
        Return the address for this delivery.
        :return: self._address
        """
        return self._address

    def get_deliverer(self):
        """
        Return the deliverer for this delivery.
        :return: self._deliverer
        """
        return self._deliverer
