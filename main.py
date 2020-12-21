import requests
from typing import Optional

"""
The main class of the program - for the customer.
"""

NOT_UNDERSTAND = "We could not understand what you typed. Please try again."
ORDER_NOT_FOUND = "Sorry, this order doesn't exist."
ITEM_NOT_FOUND = "This type of item does not exist. Please try again.\n"

LOCALHOST = "http://127.0.0.1:5000/"


def add_item() -> None:
    """
    Ask the user for information of an item, and add it to an order, as long
    as the order is valid.
    """
    b = is_valid_order()
    if not b[0]:
        return
    order_num = b[1]
    print("Here are all the items you can add:")
    print("\t1. Pizzas\n\t2. Drinks\n\t3. Sides\n\t4. Nothing")
    item_num = input("Which item would you like to add? Type the number "
                     "corresponding to your choice: ")

    if item_num == "1":
        item_type = "Pizzas"
    elif item_num == "2":
        item_type = "Drinks"
    elif item_num == "3":
        item_type = "Sides"
    elif item_num == "4":
        return
    else:
        print(NOT_UNDERSTAND)
        return

    item_name = _find_type(item_type)

    if item_name[1] is None:
        return
    elif item_name[1] is True:
        return
    else:
        item = _add_specific_item(item_name[0], item_type, False)

    item_details = {
        "Order Number": order_num,
        "Item Type": item_type,
        "Item Name": item_name,
        "Item Quantity": item["Quantity"]
    }
    if item_type == "Pizzas":
        item_details["Toppings"] = item["Toppings"]
        item_details["ToppingsAmount"] = item["ToppingsAmount"]
        item_details["Size"] = item["Size"]
    elif item_type == "Drinks":
        item_details["Ice"] = item["Ice"]
        item_details["Size"] = item["Size"]

    response = requests.get(LOCALHOST + "add-item", params=item_details)
    resp = response.json()

    if resp["Status Code"] == 200:
        print("Item added to your cart.\n")
    elif response.status_code != 200:
        print("Could not add item to cart.")


def _add_specific_item(item_name: str, item_type: str, b: bool) -> \
        dict:
    """
    Helper function for add_item.
    """
    if item_type == "Pizzas":
        return _add_pizza(item_name, b)
    elif item_type == "Drinks":
        return _add_drink(item_name)
    else:
        return _add_side(item_name)


def _add_pizza(item_name: str, b: bool) -> Optional[dict]:
    """
    Helper function for _add_specific_item.
    """
    p = {}
    if not b:
        quantity = input("How many {} pizzas would you like? Type a "
                         "whole number: ".format(item_name))
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError

            p["Quantity"] = quantity

            toppings = _find_type("Toppings")
            if len(toppings) == 3:
                p["Toppings"] = toppings[0]
                p["ToppingsAmount"] = toppings[2]

            size = _find_type("PizzaSizes")[0]
            p["Size"] = size
        except ValueError:
            print(NOT_UNDERSTAND)
            return
        return p


def _add_drink(item_name: str) -> Optional[dict]:
    """
    Helper function for _add_specific_item.
    """
    p = {}
    quantity = input("How many {} drinks would you like? Type a "
                     "whole number: ".format(item_name))
    try:
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError

        p["Quantity"] = quantity

        ice = input("Would you like ice in your drink? Type 1 for yes, "
                    "2 for no: ")
        if ice in ["1", "2"]:
            p["Ice"] = ice

        size = _find_type("DrinkSizes")
        p["Size"] = size
    except ValueError:
        print(NOT_UNDERSTAND)
        return
    return p


def _add_side(item_name: str) -> Optional[dict]:
    """
    Helper function for _add_specific_item.
    """
    p = {}
    quantity = input("How many {} would you like? Type a "
                     "whole number: ".format(item_name))
    try:
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError

        p["Quantity"] = quantity

        sauces = input("How many sauces would you like? Type a whole number: ")
        sauces = int(sauces)
        if sauces < 0:
            raise ValueError

        p["Sauces"] = sauces
    except ValueError:
        print(NOT_UNDERSTAND)
        return
    return p


def create_order() -> None:
    """
    Create an order, giving it a new order number.
    """
    resp = requests.get(LOCALHOST + "create-order")
    details = resp.json()
    if details["Status Code"] == 200:
        print("You have been assigned order number {}.".format(
            details["Order Number"]))
    else:
        print("Order could not be created.")


def is_valid_order() -> tuple:
    """
    Checks if an order exists, given its order number.
    :return: tuple where first value is a boolean, and second is either None or
    the number of the order. None means the order doesn't exist.
    """
    order_num = input("What is the order number of the order you want to "
                      "select? ")
    try:
        order_num = int(order_num)
    except ValueError:
        print(NOT_UNDERSTAND)
        return False,
    order = {
        "OrderNumber": order_num
    }
    resp = requests.get(LOCALHOST + "valid-order", params=order)
    details = resp.json()
    if details["Status Code"] == 204:
        print(ORDER_NOT_FOUND)
    elif details["Status Code"] == 404:
        print("Order hasn't been cancelled due to a connection error.")
    else:
        return True, order_num
    return False,


def show_order() -> None:
    """
    Show the total order, given its order number.
    """
    order_num = input("What is the order number of the order you want to see? ")
    try:
        order_num = int(order_num)
    except ValueError:
        print(NOT_UNDERSTAND)
        return
    order = {
        "OrderNumber": order_num
    }
    resp = requests.get(LOCALHOST + "show-order", params=order)
    details = resp.json()
    if details["Status Code"] == 204:
        print(ORDER_NOT_FOUND)
    elif details["Status Code"] == 404:
        print("Order hasn't been processed due to a connection error.")
    else:
        print(details["Order"])


def checkout_order() -> None:
    """
    Finalize and checkout an order, and send it for delivery.
    """
    b = is_valid_order()
    if not b[0]:
        return
    order_num = b[1]

    print("Here are the options for ordering:")
    print("\t1. Dine-in\n\t2. PizzaParlour's own delivery\n\t3. UberEats\n\t4."
          " Foodora")

    company = input("How would you like to order? Type the number corresponding"
                    " to your choice: ")
    if company not in ["1", "2", "3", "4"]:
        return

    address = ""
    if company != "1":
        address = input("Please type your address for delivery: ")
    order = {
        "OrderNumber": order_num,
        "Address": address,
        "Company": company
    }
    resp = requests.get(LOCALHOST + "checkout-order", params=order)
    details = resp.json()
    if details["Status Code"] == 204:
        print(ORDER_NOT_FOUND)
    elif details["Status Code"] == 200:
        if details["Notification"] is not None:
            print(details["Notification"])
    else:
        print("Order couldn't be delivered due to a connection error.")


def cancel_order() -> None:
    """
    Cancel an existing order.
    """
    num = input("What is the order number of the order you want to cancel? ")
    try:
        num = int(num)
    except ValueError:
        print(NOT_UNDERSTAND)
        return

    order = {
        "OrderNumber": num
    }
    resp = requests.get(LOCALHOST + "cancel-order", params=order)
    details = resp.json()
    if details["Status Code"] == 204:
        print(ORDER_NOT_FOUND)
    elif details["Status Code"] == 404:
        print("Order couldn't be cancelled due to a connection error.")
    else:
        print("Your order has been cancelled.")


def show_menu() -> None:
    """
    Show the entire menu to the customer.
    """
    resp = requests.get(LOCALHOST + "show-menu")
    details = resp.json()
    if details["Status Code"] == 200:
        print(details["Menu"])


def _find_type(item_type: str) -> Optional[tuple]:
    """
    Return the flavour a customer wants based of the type of the item.
    :param item_type: Type of the item.
    :return: tuple
    """
    items = {
        "ItemName": item_type
    }
    resp = requests.get(LOCALHOST + "flavours", params=items)
    flavours = resp.json()["Flavours"]

    print("Here are all the {} types:".format(item_type))
    for i in range(len(flavours)):
        print("\t{}. {}".format(i + 1, flavours[i]))

    if item_type not in ["PizzaSizes", "DrinkSizes"]:
        print("\t{}. Nothing".format(len(flavours) + 1))
    flav = input("Which type would you like to get? Type the number "
                 "corresponding to your choice: ")
    try:
        flav = int(flav)
    except ValueError:
        print("We could not understand what you typed.\n")
        return

    if flav in [i + 1 for i in range(len(flavours))]:
        if item_type == "Toppings":
            amount = input("How many {} do you want? Type a whole "
                           "number: ".format(flavours[flav - 1]))
            try:
                amount = int(amount)
            except ValueError:
                print(NOT_UNDERSTAND)
                return
            return flavours[flav - 1], item_type, amount

        return flavours[flav - 1], item_type
    elif flav == len(flavours) + 1:
        return "Nothing", True
    return None, None


def find_menu_item() -> None:
    """
    Find a specific menu item, given the item's information.
    """
    print("Here are all the item types on the menu:")
    print("\t1. Pizzas\n\t2. Drinks\n\t3. Toppings\n\t4. Sides")

    item_type = input("Which type of item would you like to search for? Type "
                      "the number corresponding to your choice: ")
    t = None
    if item_type == "1":
        t = _find_type("Pizzas")
    elif item_type == "2":
        t = _find_type("Drinks")
    elif item_type == "3":
        t = _find_type("Toppings")
    elif item_type == "4":
        t = _find_type("Sides")

    if not t:
        print(ITEM_NOT_FOUND)
    else:
        result = {
            "ItemName": t[0],
            "ItemType": t[1]
        }
        resp = requests.get(LOCALHOST + "find-item", params=result)
        item = resp.json()

        if item["Status Code"] == 204:
            print(ITEM_NOT_FOUND)
        else:
            print(item["Item"])


def do_command() -> None:
    """
    Perform a specific command the user asks for.
    """
    print("Here are your options:")
    print("\t1. Create a new order")
    print("\t2. Add item to an order")
    print("\t3. Show the total order")
    print("\t4. Checkout order for delivery")
    print("\t5. Cancel an existing order")
    print("\t6. Show the menu")
    print("\t7. Find a specific item from the menu")
    print("\t8. Exit the program")

    cmd = input("\nWhat would you like to do? Type the number corresponding to "
                "your choice: ")
    if cmd == "1":
        create_order()
    elif cmd == "2":
        add_item()
    elif cmd == "3":
        show_order()
    elif cmd == "4":
        checkout_order()
    elif cmd == "5":
        cancel_order()
    elif cmd == "6":
        show_menu()
    elif cmd == "7":
        find_menu_item()
    elif cmd == "8":
        return
    else:
        print(NOT_UNDERSTAND)

    print("\n")
    do_command()


def run() -> None:
    """
    Main function.
    """
    print("Hi! Welcome to Pizza Parlour.")
    show_menu()
    do_command()


if __name__ == '__main__':
    run()
