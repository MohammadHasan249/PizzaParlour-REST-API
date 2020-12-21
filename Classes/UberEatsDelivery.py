import json
from Classes.Delivery import Delivery

UBER_EATS = "Uber Eats"


class UberEatsDelivery(Delivery):
    """
    A delivery that Uber Eats has to make.

    === Private Attributes ===
    _file: The file to save the order to.
    """
    _file: str  # THIS SHOULD BE A JSON FILE!

    def __init__(self, order, file):
        """
        Initialize an UberEatsDelivery object.
        :param file: The json file to store the order in.
        """
        super().__init__(order, UBER_EATS)
        self._file = file

    def deliver(self):
        """
        Deliver the order.
        :return A string if the delivery was saved successfully. None otherwise.
        """
        result = self.make_dict()
        if not self._file.endswith(".json"):
            return None
        try:
            with open(self._file, 'w') as json_file:
                json.dump(result, json_file)
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
