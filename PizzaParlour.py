from flask import Flask, request, jsonify

from Classes.DeliveryFactory import DeliveryFactory
from Classes.Order import Order
# # from Classes.Delivery import Delivery
from Classes.Menu import Menu
from Classes.MenuItem import MenuItem
# from Classes.Pizza import Pizza
# from Classes.Drink import Drink
import json
from Classes.ItemFactory import ItemFactory

app = Flask("Assignment 2")
FILENAME = "Menu.txt"

# dict from order_number to Order object
orders = {}
ORDER_NUM = 1


@app.route('/flavours')
def get_flavours():
    """
    Get all the flavours of an item.
    """
    _menu = _read_from_file()
    item_dict = request.args.to_dict(flat=False)
    item_name = item_dict["ItemName"][0]
    flavours = _menu.get_names(item_name)
    result = {
        "Flavours": flavours
    }
    return jsonify(result)


@app.route('/add-item')
def add_item():
    """
    Create an item and add it to an order, given the item's information.
    """
    _menu = _read_from_file()
    item_dict = request.args.to_dict(flat=False)
    order_num = item_dict["Order Number"][0]
    order = orders[order_num]
    item_type = item_dict["Item Type"][0]
    item_name = item_dict["Item Name"][0]
    item_amt = int(item_dict["Item Quantity"][0])

    factory = ItemFactory()
    menu_item = _menu.get_item(item_name, item_type)

    if item_type == "Pizzas":
        toppings = item_dict["Toppings"]
        print(toppings)
        toppings_amount = item_dict["ToppingsAmount"][0]
        print(toppings_amount)
        size = item_dict["Size"][0]
        size_item = _menu.get_item(size, "PizzaSizes")
        item = factory.create_item(menu_item, size_item)
        for t in toppings:
            if t != "Nothing":
                topping = _menu.get_item(t, "Toppings")
                item.set_topping(topping, int(toppings_amount))
    elif item_type == "Drinks":
        ice = item_dict["Ice"][0]
        size = item_dict["Size"][0]
        size_item = _menu.get_item(size, "DrinkSizes")
        item = factory.create_item(menu_item, size_item)
        if ice == "1":
            item.set_ice(True)
        else:
            item.set_ice(False)
    else:
        item = factory.create_item(menu_item)
    item.set_amount(item_amt)

    order.add_to_cart(item)
    result = {
        "Status Code": 200
    }
    return jsonify(result)


@app.route('/find-item')
def find_item():
    """
    Find an item from the Menu, given its information.
    """
    _menu = _read_from_file()
    item_dict = request.args.to_dict(flat=False)
    print(item_dict)
    item_type = item_dict["ItemType"][0]
    item_name = item_dict["ItemName"][0]
    print(item_name, type(item_name))
    print(item_type, type(item_type))

    item = _menu.get_item(item_name, item_type)

    item_str = ""
    if item:
        item_str = "{} {}: ${}".format(item_name, item_type, item.get_price())

    result = {
        "Item": item_str,
        "Status Code": 200
    }

    if not item:
        result["Status Code"] = 204

    return jsonify(result)


@app.route('/create-order')
def create_order():
    """
    Create an order with an order number, if an order with this order number
    doesn't already exist.
    """
    global ORDER_NUM
    order = Order(ORDER_NUM)
    orders[str(ORDER_NUM)] = order
    result = {
        "Order Number": ORDER_NUM,
        "Status Code": 200
    }
    ORDER_NUM += 1
    return jsonify(result)


@app.route('/checkout-order')
def checkout_order():
    """
    Finalize and checkout an order, and send it for delivery.
    """
    order_details = request.args.to_dict(flat=False)
    order_num = order_details["OrderNumber"][0]
    order = None

    if order_num in list(orders.keys()):
        order = orders[order_num]

    company = order_details["Company"][0]
    address = order_details["Address"][0]

    factory = DeliveryFactory()
    ret = ""

    if company == "1":
        ret = "Please take a seat, your order will be at your table shortly."
    elif company == "2":
        delivery = factory.create_delivery(order, "PizzaParlour")
        delivery.set_address(address)
        delivery.deliver()
        ret = "Delivery by Pizza Parlour successful passed through. Your " \
              "order will be there shortly."
    elif company == "3":
        delivery = factory.create_delivery(order, "Uber Eats", "UberEats.json")
        delivery.set_address(address)
        delivery.deliver()
        ret = "Delivery by Uber Eats successful passed through. Your " \
              "order will be there shortly."
    elif company == "4":
        delivery = factory.create_delivery(order, "Foodora", "Foodora.csv")
        delivery.set_address(address)
        delivery.deliver()
        ret = "Delivery by Foodora successfully passed through. Your " \
              "order will be there shortly."

    result = {
        "Notification": ret,
        "Status Code": 200
    }

    if not order:
        result["Status Code"] = 204

    if order_num in list(orders.keys()):
        del orders[order_num]

    return jsonify(result)


@app.route('/cancel-order')
def cancel_order():
    """
    Cancel an existing order.
    """
    order_details = request.args.to_dict(flat=False)
    order_num = order_details["OrderNumber"][0]
    order = None

    if order_num in list(orders.keys()):
        del orders[order_num]
        code = 200
    else:
        code = 204

    result = {
        "Status Code": code
    }

    return jsonify(result)


@app.route('/valid-order')
def valid_order():
    """
    Check if an order exists.
    :return:
    """
    order_details = request.args.to_dict(flat=False)
    order_num = order_details["OrderNumber"][0]

    valid = False
    if order_num in list(orders.keys()):
        valid = True

    result = {
        "Valid": valid,
        "Status Code": 200
    }

    if not valid:
        result["Status Code"] = 204

    return jsonify(result)


@app.route('/show-order')
def show_order():
    """
    Show an order to the customer, given its order number.
    """
    order_details = request.args.to_dict(flat=False)
    order_num = order_details["OrderNumber"][0]
    order = None

    if order_num in list(orders.keys()):
        order = orders[order_num]

    result = {
        "Order": order.__str__(),
        "Status Code": 200
    }

    if not order:
        result["Status Code"] = 204
    else:
        result["Order"] = order.__str__()

    return jsonify(result)


@app.route('/show-menu')
def show_menu():
    """
    Show the Menu to the customer.
    """
    menu = _read_from_file()
    menu_dict = {
        "Menu": menu.__str__(),
        "Status Code": 200
    }
    return jsonify(menu_dict)


def _read_from_file() -> Menu:
    """
    Read Menu items from a file, and initialize and return a Menu with the
    information read.
    """
    menu = Menu()
    with open(FILENAME) as f:
        menu_dict = json.load(f)

    for t in menu_dict:
        flavours = menu_dict[t]
        for l in flavours:
            if t == "Pizzas" or t == "Drinks":
                item = MenuItem(l[0], t, True, l[1], 1)
            else:
                item = MenuItem(l[0], t, False, l[1], 1)
            menu.add_item(item)
    return menu


if __name__ == "__main__":
    app.run()
