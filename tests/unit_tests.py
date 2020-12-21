import PizzaParlour
from main import run
from Classes.Menu import Menu, MENU_GREETING_MSG
from Classes.MenuItem import MenuItem, AMOUNT
from Classes.Pizza import Pizza, TOPPINGS, SIZE_UPGRADE
from Classes.Drink import Drink, ICE
from Classes.Side import Side, SAUCES
from Classes.Order import Order, ORDER_INTRODUCTION_MSG
from Classes.ItemFactory import ItemFactory
from Classes.Delivery import Delivery
from Classes.UberEatsDelivery import UberEatsDelivery, UBER_EATS
from Classes.FoodoraDelivery import FoodoraDelivery, FOODORA
from Classes.DeliveryFactory import DeliveryFactory
from tests.input_test import get_display_output, set_keyboard_input


def test_menu_and_menu_item_classes():
    """
    Test all methods inside the Menu and MenuItem classes. Also tests the
    function in Menu.py
    """
    # We test MenuItem methods first
    # __init__()
    item1 = MenuItem("item1", "type1", True, 10.0, 1)
    item2 = MenuItem("item2", "type1", True, 15.0, 1)
    identical_to_item1 = MenuItem("item1", "type1", True, 10.0, 1)

    # __eq__()
    assert item1 != item2
    assert item1 == identical_to_item1
    # __str__()
    assert item1.__str__() == "item1: $10.00\n"
    # Getter methods
    assert item1.get_name() == "item1"
    assert item1.get_type() == "type1"
    assert item1.get_sellable()
    assert item1.get_price() == 10.0
    assert item1.get_amount() == 1
    assert item1.get_attributes() == [AMOUNT]
    # Setter methods
    item1.set_amount(3)
    assert item1.get_amount() == 3
    item1.set_attribute(AMOUNT, 1)
    assert item1.get_amount() == 1

    # We test Menu methods now
    # __init__()
    menu = Menu()

    # add_item()
    assert not menu.add_item(item1)
    # get_item()
    assert menu.get_item("item1", "type1")
    assert not menu.get_item("DNE", "DNE")

    menu.add_item(item2)
    menu.add_item(identical_to_item1)
    item3 = MenuItem("item3", "type2", False, 12.03, 1)
    menu.add_item(item3)
    # __str__()
    print_menu = menu.__str__()
    expected_str = MENU_GREETING_MSG + "type1:\n\titem1: $10.00\n\titem2: " \
                                       "$15.00\n"
    expected_str += "type2:\n\titem3: $12.03\n"
    assert print_menu == expected_str

    # get_names()
    assert menu.get_names("type1") == ["item1", "item2"]


def test_pizza_class():
    """
    Test all methods inside the Pizza class.
    """
    # __init__()
    small = MenuItem("Small", "Pizza size", False, 0.0, 1)
    medium = MenuItem("Medium", "Pizza size", False, 4.0, 1)
    topping1 = MenuItem("Extra cheese", "Topping", False, 2.0, 1)
    topping2 = MenuItem("Special sauce", "Topping", False, 3.0, 1)
    pizza_menu_item1 = MenuItem("Pepperoni", "Pizzas", True, 10.0, 1)
    pizza_menu_item2 = MenuItem("Meatball", "Pizzas", True, 12.0, 1)
    pizza1 = Pizza(pizza_menu_item1, small)
    pizza2 = Pizza(pizza_menu_item2, small)
    pizza3 = Pizza(pizza_menu_item1, medium)
    # __eq__()
    assert pizza1 != pizza3
    assert pizza1 != pizza2
    pizza3.set_size(small)
    assert pizza1 == pizza3

    # Getter methods except get_price()
    assert pizza1.get_toppings() == []
    assert pizza1.get_size() == small
    assert pizza1.get_attributes() == [AMOUNT, TOPPINGS, SIZE_UPGRADE]

    # Setter methods
    pizza1.set_attribute(TOPPINGS, {topping1: 2})
    assert pizza1.get_toppings()[0].get_amount() == 2
    pizza1.set_attribute(AMOUNT, 2)
    assert pizza1.get_amount() == 2
    pizza1.set_attribute(SIZE_UPGRADE, small)
    assert pizza1.get_size() == small
    pizza1.set_size(medium)
    assert pizza1.get_size() == medium
    pizza1.set_topping(topping1, 3)
    assert pizza1.get_toppings()[0].get_amount() == 3
    pizza1.set_topping(topping2, 1)
    assert pizza1.get_toppings()[1].get_amount() == 1
    pizza1.set_amount(1)
    # get_price()
    assert pizza1.get_price() == 23

    # __str__()
    topping1_str = "\t\t3 Extra cheese\n"
    topping2_str = "\t\t1 Special sauce\n"
    expected_str = "($23.00) 1 Medium Pepperoni pizza(s) with the " \
                   "following toppings:\n" + topping1_str + topping2_str
    assert pizza1.__str__() == expected_str

    # _check_toppings()
    pizza3.set_topping(topping1, 3)
    pizza3.set_topping(topping2, 1)
    assert pizza1._check_toppings(pizza3)
    pizza3.set_topping(topping1, 0)
    assert not pizza1._check_toppings(pizza3)
    pizza3.set_topping(topping1, 1)
    assert not pizza1._check_toppings(pizza3)
    pizza3.set_topping(topping1, 0)
    pizza1.set_topping(topping2, 0)
    assert not pizza1._check_toppings(pizza3)


def test_drink_class():
    """
    Test all methods inside the Drink class.
    """
    # __init__()
    default_size = MenuItem("Small size", "Drink size", False, 0.0, 1)
    size_upgrade = MenuItem("Medium size", "Drink size", False, 1.0, 1)
    drink_menu_item1 = MenuItem("Coca Cola", "Drinks", True, 1.0, 1)
    drink_menu_item2 = MenuItem("Fanta", "Drinks", True, 1.5, 1)
    drink1 = Drink(drink_menu_item1, default_size)
    drink2 = Drink(drink_menu_item2, default_size)
    drink3 = Drink(drink_menu_item1, size_upgrade)
    drink3.set_ice(False)
    # Getter methods except get_price
    assert drink1.get_ice()
    assert drink1.get_size() == default_size
    assert drink1.get_attributes() == [AMOUNT, ICE, SIZE_UPGRADE]
    # Setter methods and __eq__()
    assert drink1 != drink2
    drink1.set_size(size_upgrade)
    assert drink1.get_size() == size_upgrade
    drink1.set_ice(False)
    assert not drink1.get_ice()
    drink1.set_amount(2)
    assert drink1.get_amount() == 2
    assert drink1 == drink3
    # get_price()
    assert drink1.get_price() == 4.0

    expected_str = "($4.00) 2 Medium size Coca Cola drink(s) with no ice.\n"
    assert drink1.__str__() == expected_str
    drink1.set_ice(True)
    expected_str = "($4.00) 2 Medium size Coca Cola drink(s) with ice.\n"
    assert drink1.__str__() == expected_str

    # set_attributes()
    drink1.set_attribute(AMOUNT, 312)
    assert drink1.get_amount() == 312
    drink1.set_attribute(ICE, True)
    assert drink1.get_ice()
    drink1.set_attribute(SIZE_UPGRADE, default_size)
    assert drink1.get_size() == default_size


def test_side_class():
    """
    Test all methods inside the Side class.
    """
    # __init__()
    side_menu_item1 = MenuItem("Fries", "Sides", True, 4.0, 1)
    side_menu_item2 = MenuItem("Salad", "Sides", True, 3.0, 1)
    side1 = Side(side_menu_item1)
    side2 = Side(side_menu_item2)
    side3 = Side(side_menu_item1)
    # Getter methods
    assert side1.get_sauces() == 1
    assert side1.get_attributes() == [AMOUNT, SAUCES]

    # Setter methods and __eq__()
    side1.set_sauces(3)
    side2.set_sauces(3)
    side3.set_sauces(2)
    assert side1 != side2
    assert side1 != side3
    side3.set_sauces(3)
    assert side3.get_sauces() == 3
    assert side1 == side3
    side3.set_attribute(SAUCES, 1)
    assert side3.get_sauces() == 1
    side3.set_attribute(AMOUNT, 2)
    assert side3.get_amount() == 2

    expected_price = 4.0
    assert side1.get_price() == expected_price

    expected_str = "($4.00) 1 Fries with 3 sauces each.\n"
    assert side1.__str__() == expected_str


def test_item_factory_class():
    """
    Test all methods inside the ItemFactory class.
    """
    # __init__()
    factory = ItemFactory()
    pizza_menuitem = MenuItem("cheese", "Pizzas", True, 10.0, 1)
    drink_menuitem = MenuItem("fanta", "Drinks", True, 10.0, 1)
    side_menuitem = MenuItem("fries", "Sides", True, 10.0, 1)
    none_menuitem = MenuItem("oreo", "oreo", True, 10.0, 1)
    medium = MenuItem("medium", "size", False, 4.0, 1)

    # create_item()
    expected_pizza = Pizza(pizza_menuitem, medium)
    expected_drink = Drink(drink_menuitem, medium)
    expected_side = Side(side_menuitem)
    pizza = factory.create_item(pizza_menuitem, medium)
    assert pizza == expected_pizza
    assert factory.create_item(drink_menuitem, medium) == expected_drink
    assert factory.create_item(side_menuitem) == expected_side
    assert not factory.create_item(none_menuitem, medium)


def test_order_and_delivery_class():
    """
    Test all methods inside the Order and Delivery classes.
    """
    # Test Order methods first
    # __init__()
    order = Order(1)
    cheese = MenuItem("cheese", "Pizzas", True, 10.00, 1)
    fanta = MenuItem("fanta", "Drinks", True, 1.00, 1)
    fries = MenuItem("fries", "Sides", True, 5.00, 1)
    extra_mushroom = MenuItem("extra mushrooms", "toppings", False, 1.00, 1)
    medium = MenuItem("medium", "size", False, 5.00, 1)

    pizza = Pizza(cheese, medium)
    pizza.set_topping(extra_mushroom, 2)
    drink = Drink(fanta, medium)
    side = Side(fries)

    # Getter methods except price
    assert order.get_cart() == []
    assert order.get_order_number() == 1

    # add_to_cart(), remove_from_cart(), and set_item()
    order.add_to_cart(pizza)
    order.add_to_cart(drink)
    order.add_to_cart(side)
    assert len(order.get_cart()) == 3
    assert order.remove_from_cart(1)
    assert not order.remove_from_cart(3242)
    assert len(order.get_cart()) == 2
    order.add_to_cart(pizza)
    order.add_to_cart(pizza)
    assert order.get_cart()[2].get_amount() == 2

    wrong_input = {"position": 432}
    input_dict = {"position": 1, "attributes": {ICE: False}}
    assert not order.set_item(wrong_input)
    assert order.set_item(input_dict)
    assert not drink.get_ice()

    # get_total_price()
    assert order.get_total_price() == pizza.get_price() + drink.get_price() + \
           side.get_price()

    # _get_equivalent_item()
    none_item = MenuItem("none", "none", True, 234.00, 32)
    assert not order._get_equivalent_item(none_item)

    # is_valid_position
    assert order.is_valid_position(1)
    assert not order.is_valid_position(34523)

    # __str__()
    expected_str = "Your order number is 1.\n" + ORDER_INTRODUCTION_MSG + \
                   "\t" + drink.__str__() + "\t" + side.__str__() + "\t" + \
                   pizza.__str__() + \
                   "\nThe total price is ${:.2f}.".format(
                       order.get_total_price())
    assert expected_str == order.__str__()

    # Test Delivery methods
    # __init__()
    delivery = Delivery(order, "pizza place")

    # deliver() and set_address()
    assert not delivery.deliver()
    delivery.set_address("42 Corniche St.")
    assert delivery.deliver()

    # Getter methods
    assert delivery.get_order().get_cart() == order.get_cart()
    assert delivery.get_address() == "42 Corniche St."
    assert delivery.get_deliverer() == "pizza place"

    # make_dict()
    expected_dict = {"Order Number": 1,
                     "Address": "42 Corniche St.",
                     "Order Details": order.__str__()}
    assert expected_dict == delivery.make_dict()


def test_delivery_subclasses():
    """
    Tests methods of all Delivery subclasses.
    """
    # Start with UberEatsDelivery class
    # __init__()
    order = Order(1)
    fries = MenuItem("fries", "Sides", True, 5.00, 1)
    order.add_to_cart(fries)
    uber_eats = UberEatsDelivery(order, "Test1.json")
    deliver_error = UberEatsDelivery(order, "FileDoesNotExist.jsdson")
    uber_eats.set_address("some address")

    # Getter methods
    assert uber_eats.get_file() == "Test1.json"
    assert uber_eats.get_deliverer() == UBER_EATS

    # deliver()
    assert uber_eats.deliver()
    assert not deliver_error.deliver()

    # FoodoraDelivery class
    # __init__()
    foodora = FoodoraDelivery(order, "Test2.csv")
    deliver_error = FoodoraDelivery(order, "FileDoesNotExist.cdwasv")
    foodora.set_address("some address")

    # Getter methods
    assert foodora.get_file() == "Test2.csv"
    assert foodora.get_deliverer() == FOODORA

    # deliver()
    assert foodora.deliver()
    assert not deliver_error.deliver()


def test_delivery_factory_class():
    """
    Test all methods in DeliveryFactory class.
    """
    # __init__()
    factory = DeliveryFactory()
    order = Order(1)
    file = "This is a file."

    expected_uber = UberEatsDelivery(order, file)
    expected_foodora = FoodoraDelivery(order, file)
    expected_delivery = Delivery(order, "not uber or foodora")

    assert factory.create_delivery(order, UBER_EATS, file).get_deliverer() == \
           expected_uber.get_deliverer()
    assert factory.create_delivery(order, FOODORA, file).get_deliverer() == \
           expected_foodora.get_deliverer()
    assert factory.create_delivery(order, "not uber or foodora", file).\
               get_deliverer() == expected_delivery.get_deliverer()


def test_main_pizza_parlour_one():
    """
    Test case of main and PizzaParlour classes when a customer orders a pizza
    and dines in.
    """
    inputs = ["1", "2", "1", "1", "1", "1", "1", "2", "3", "3", "1", "4", "1",
              "1", "8"]
    set_keyboard_input(inputs)

    run()

    output = get_display_output()

    expected = "\t8. Exit the program"
    assert output[-2] == expected


def test_main_pizza_parlour_two():
    """
    Test case of main and PizzaParlour classes when a customer orders a pizza, a
    drink, a side item and then Uber Eats it.
        """
    inputs = [1, 2, 1, 1, 1, 1, 1, 2, 3, 3, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2,
                  2, 1, 2, 1, 3, 1, 123, 123, 4, 1, 3, "Corniche", 8]

    mock_inputs = [str(i) for i in inputs]
    set_keyboard_input(mock_inputs)

    run()

    output = get_display_output()

    expected = "\t8. Exit the program"

    assert output[-2] == expected


def test_parlour_one():
    """
    Test pizza parlour's read from file.
    """
    menu = 'Here is our menu:\nPizzas:\n\tMargherita: $10.99\n\t' \
           'Pepperoni: $12.99\nDrinks:\n\tSprite: $2.99\n\tPepsi: $3.99\n' \
           'PizzaSizes:\n\tSmall: $0.00\n\tMedium: $3.99\n\tLarge: $6.99\n' \
           'DrinkSizes:\n\tSmall: $0.00\n\tMedium: $2.99\n\tLarge: $4.99\n' \
           'Toppings:\n\tExtra Cheese: $1.99\nSides:\n\tFries: $6.99\n'

    assert PizzaParlour._read_from_file().__str__() == menu


def test_parlour_two():
    """
    Test pizza parlour's show_menu function.
    """
    response = PizzaParlour.app.test_client().get('/show-menu')

    assert response.status_code == 200
