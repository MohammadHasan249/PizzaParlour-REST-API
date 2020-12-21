from Classes.MenuItem import MenuItem
from typing import List, Optional

ORDER_INTRODUCTION_MSG = "Your order is as follows:\n"
NO_ORDER_MSG = "Your order is empty."


class Order:
    """
    A client's order to be sent to the Pizza Parlour.

    === Private Attributes ===
    _cart: contains all the items that the client wants to buy.
    """
    _order_number = int
    _cart: List[MenuItem]

    def __init__(self, order_number: int) -> None:
        """
        Initialize an order.
        :param order_number: The order number for this Order. It is assumed to
        be unique.
        """
        self._cart = []
        self._order_number = order_number

    def __str__(self) -> str:
        """
        Used when self is passed into print() method.
        :return: A string representation of the information in this Order.
        """
        ret = NO_ORDER_MSG
        if len(self._cart) > 0:
            ret = "Your order number is {}.\n".format(self._order_number)
            ret += ORDER_INTRODUCTION_MSG
            for i in range(len(self._cart)):
                item = self._cart[i]
                ret += "\t{}".format(item.__str__())
            ret += "\nThe total price is ${:.2f}.".format(
                self.get_total_price())
        return ret

    def get_total_price(self) -> float:
        price = 0.0
        for item in self._cart:
            price += item.get_price()
        return price

    def add_to_cart(self, item: MenuItem) -> None:
        """
        Adds item to the cart.
        :param item: item to be added to the order.
        """
        cart_item = self._get_equivalent_item(item)
        if cart_item:
            cart_item.set_amount(cart_item.get_amount() + item.get_amount())
        else:
            self._cart.append(item)

    def remove_from_cart(self, position: int) -> bool:
        """
        Remove the item at index position - 1.
        :param position: Position of the item to be removed (index + 1).
        :return whether or not the item at that position was successful.
        """
        if 0 <= position - 1 <= len(self._cart):
            self._cart.pop(position - 1)
            return True
        return False

    def set_item(self, item_info) -> bool:
        """
        Alter the item located at position position of the order to the client's
        will.
        :param item_info: A dictionary representing the information of the item
         to change.
        """
        pos = item_info["position"]
        if not self.is_valid_position(pos):
            return False

        item = self._cart[pos - 1]
        attributes = item_info["attributes"]
        for a in attributes:
            item.set_attribute(a, attributes[a])

        return True

    def is_valid_position(self, pos: int):
        """
        Return whether or not the position entered by the client is valid for
        this order.
        :param pos: The position input from the client.
        :return: True if it is valid for this order. False otherwise.
        """
        return 0 <= (pos - 1) < len(self._cart)

    # Getter methods

    def get_order_number(self) -> int:
        """
        Return the order's order number
        :return: self._order_number
        """
        return self._order_number

    def get_cart(self) -> List[MenuItem]:
        """
        Return the order's cart.
        :return: self._cart
        """
        return self._cart

    # Helper methods

    def _get_equivalent_item(self, item: MenuItem) -> Optional[MenuItem]:
        """
        Return an item in this order if it is equivalent to item.
        :param item: The item in question.
        :return: The relevant item in this order if it exists. Return None
        otherwise.
        """
        for cart_item in self._cart:
            if type(cart_item) == type(item) and cart_item == item:
                return cart_item
        return None
