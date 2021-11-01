menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
* Quit anytime by type: exit or x *
***********************************
"""

listMune = """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""

coustmerList = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}


def menuOrder():
    print(menu)
    while (True):
        print("**you can Quit anytime by type: exit or x**")
        addIteam = input("would you like to add anything else?  ").capitalize()

        if addIteam in coustmerList:
            coustmerList[addIteam] += 1
            for i in coustmerList:
                if int(coustmerList[i]) > 0:
                    print(f"{coustmerList[i]} item of {i}")

        if (addIteam == "Exit" or addIteam == "X" or addIteam == "Quit"):
            exit("Good Bye")

        if addIteam not in coustmerList:
            print("we dont have this in our menu")
            print(f"Our mune list is: {listMune}")
            
menuOrder()
