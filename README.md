How to run the app:
    Run the main Flask module by running `python3 PizzaParlour.py`
    Next, run main.py in parallel by running `python3 main.py`
    You can also run the app in Pycharm by running PizzaParlour.py and Main.py
    in parallel

How to run tests:
    Run unit tests with coverage by running:
    pytest --cov-report term --cov=. tests/unit_tests.py
    Do not run this while PizzaParlour.py or main.py is active.
    This should be run on its own.

Pair Programming:
    Feature 1:
        Driver: Haider
        Navigator: Mohammad
        Details: We implemented the Menu and MenuItem infrastructure needed for
        the Menu to be displayed as well as for its items to be capable of being
        ordered (we have had to make some changes it later on but the Driver and
        Observer did not change).
    Feature 2:
        Driver: Mohammad
        Navigator: Haider
        Details: We implemented the Order infrastructure needed for the order 
        to be displayed as well as items being able to be ordered and changed.
        We also implemented an ItemFactory that allows us to initialize items
        directly, without needing to worry about the types of items being 
        initialized. Finally, we implemented the Delivery infrastructure that 
        allows the user to have their order delivered to their address.
    Reflection:
	    Pros: We were able to code with little to no errors because of
        this technique. It also allowed us to create cleaner code than if we had
        coded individually.
	    Cons: It might not have been worth it due to our timezone 
        differences as it was a somewhat time-consuming process (since it 
        required two people to be active at the same time which was a hurdle as 
        we both were living in different timezones, one in Ontario, Canada and 
        the other in U.A.E.) 
	    Conclusion: Although it has its pros, we do not think that this process 
	    was worth the effort. In our opinion, it would have been more worthwhile
	    to have one person code the feature and the other look at it later on at
	    a more comfortable time.

How we represented objects and the relationships between these objects:
    1) MenuItem.py holds the MenuItem class which represents the items on the menu
    to be shown to the user. It contains all the relevant information about a
    particular menu item. It is also extended by classes that represents items
    that a user orders (like Pizza, Drink, and Side objects). Note that it has
    been developed in such a way that it is easy to create a subclass of (more
    extendability). You will also observe this in many of the other classes as
    well.
    2) Menu.py holds the Menu class which represents the menu that will be
    presented to the user. You can also think of this as some kind of manager
    class for MenuItem objects.
    3) Order.py holds the Order class which represents the order that is a user
    is currently placing. It contains a list of MenuItem objects which
    represents the list of items the user is ordering. However, please note that
    none of these objects are instantiated as MenuItem objects, but rather as
    one of its subclasses. We only label this list as containing MenuItems for
    the sake of making our code easier to extend. As you examine our code, you
    will notice that we have done something similar to this in many other places
    .
    4) Pizza.py, Drink.py, and Side.py hold the Pizza, Drink, and Side classes
    respectively. The Pizza class represents a pizza being ordered by the user.
    The Drink class represents a drink being ordered by the user. The Side class
    represents a side dish being ordered by the user. Also note that both size
    and topping attributes in these classes are represented in the form of
    MenuItem objects. These 3 classes are subclasses of MenuItem. If our client
    ever wants to introduce another directly sellable type of item (like maybe
    desserts or appetizers) then they should create a class that represents it
    (like how Pizza class represents a pizza) and make sure that it extends the
    MenuItem class.
    5) Delivery.py holds the Delivery class which represents a delivery that
    needs to be made. It contains an Order object which is the order that this
    Delivery object must deliver. Note that any object instantiated as a
    Delivery object will be either a delivery made by the pizza place itself or
    will be made by a third-person party delivery service that will not record
    the order anywhere. This class has 2 subclasses which represent deliveries
    made by specific delivery services (UberEats and Foodora). It can also be 
    extended to represent more specific forms of delivery (like the 2 subclasses
    we used for this app)
    6) UberEatsDelivery.py and FoodoraDelivery.py hold the UberEatsDelivery and
    FoodoraDelivery classes whose objects represent deliveries made by UberEats
    and Foodora respectively. These 2 classes are subclasses of Delivery that
    actually save orders to some sort of file.
    7) ItemFactory.py and DeliveryFactory.py hold the ItemFactory and 
    DeliveryFactory classes. ItemFactory objects are capable of creating and
    returning items that are supposed to be added to a user's order, whereas
    DeliveryFactory objects are capable of creating and returning items that are
    supposed to be used to enforce a delivery.
    
Design of functions:
    Most, if not all, functions and methods were designed with extendability and
    generalization in mind. 
    We implemented as many useful methods as we could
    possible think of. For example, we made sure all class attributes had
    getter methods (and even setter methods if they were meant to be changed
    after the object was instantiated). 
    We also made sure to create "complete" methods capable of completing a 
    user's command by itself. However, these methods do not interact directly 
    with the user (due to our choice of using the MVC design pattern we will 
    bring up in a bit), but rather deal with the user's input in a more 
    formatted way that allows us to easily satisfy the user's commands.

Design patterns usage:
    We made heavy use of the Factory and MVC design patterns.
    The ItemFactory and DeliveryFactory classes follow the Factory design
    pattern: creating and returning different types of objects depending on the
    arguments passed into their methods (Therefore making it easy to make more
    subclasses of MenuItem and Delivery)
    Our program as a whole follows the MVC (Model View Controller) design
    pattern. The user interacts with Main.py (Controller) who manipulates what
    PizzaParlour.py does (Model) (This python file is the one that makes use of
    all the classes we discussed in one of the previous sections of this 
    document) which then sends the output to be displayed in the terminal 
    (View). We chose to make use of these 2 design patterns in particular due to
    the nature of this assignment as well as to arrange for the code to be more
    extendable.
    
Clean coding practices and tools that we used to achieve this:
    Not only did we implement useful design patterns and made sure to introduce
    classes that can easily be extended or altered (within a certain means, of
    course), but we also made sure to do so using clean coding methods and
    practices.
    Hardcoded values that we used were set as constants at the head
    of the respective file that made the most use of them.
    We made sure to create appropriate docstrings for all methods and functions
    in our code so that any programmer can easily understand the function behind
    any method/function.
    We coded using the PEP8 coding standard and made use of the SOLID principles
    , most notable of which were the Single responsibility and the Open/Closed 
    principles. The latter was likely the most applied principle in our code (
    eg. all attributes were set to private), but the former was applied 
    frequently as well (eg. ItemFactory creates items, UberEatsDelivery delivers
    an order, Order records items, etc.).

How to add new features:
    If you want a new command to be created, then start with main.py and 
    PizzaParlour.py then move on to code the actual behaviours into the classes in 
    the Classes folder (or make your own classes if the existing ones do not 
    match this new command).
    If you want to improve on an existing command (perhaps add a new item type
    or delivery type), then you should extend the relevant class (MenuItem for 
    items, Delivery for deliveries, etc.) and include them in their factories.
    If you are improving an existing command, but not adding new choices
    (refining existing ones), then you can take a look at these classes, but
    make sure that all the methods satisfy their docstrings by the time you are
    done altering them.
