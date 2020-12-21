from Classes.Delivery import Delivery
from Classes.UberEatsDelivery import UberEatsDelivery, UBER_EATS
from Classes.FoodoraDelivery import FoodoraDelivery, FOODORA


class DeliveryFactory:
    """
    Is used to create objects representing deliveries.
    """

    def __init__(self) -> None:
        """
        Initializes a DeliveryFactory object.
        """

    def create_delivery(self, order, deliverer, file=None) -> Delivery:
        """
        Create and return a Delivery object depending on the input.
        :param order: The Order object.
        :param deliverer: Who the deliverer is.
        :param file: The path to the file to store the order in.
        :return: A Delivery object satisfying the inputs.
        """
        if deliverer == UBER_EATS:
            return UberEatsDelivery(order, file)
        elif deliverer == FOODORA:
            return FoodoraDelivery(order, file)
        else:
            return Delivery(order, deliverer)
