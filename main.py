# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calc_money(q, d, n, p, drink_choice):
    """adds the coins together and returns total in a dollar amount"""
    valq = q * 25
    vald = d * 1
    valn = n * 5
    valp = p * 1
    total = (valq + vald + valn + valp)/100
    return total


def calc_change(cash, price):
    """calculates the user's change after making payment"""
    cash_back = cash - price
    return cash_back


def make_drink(drink_choice, ingredients):
    """takes the proper amount of resources from the resources dictionary base on drink selection"""
    for ingredient in ingredients:
        if ingredient == 'milk' and drink_choice == 'espresso':
            ingredients[ingredient] = ingredients[ingredient]
        elif ingredients[ingredient] - MENU[drink_choice]["ingredients"][ingredient] < 0:
            print(f"There's not enough {ingredient}!")
            return ingredient
        else:
            ingredients[ingredient] -= MENU[drink_choice]["ingredients"][ingredient]
    return ingredients


def unmake_drink(drink_choice, ingredients):
    for ingredient in ingredients:
        if ingredient == 'milk' and drink_choice == 'espresso':
            ingredients[ingredient] = ingredients[ingredient]
        else:
            ingredients[ingredient] += MENU[drink_choice]["ingredients"][ingredient]
    return ingredients


def add_ingredients(ingredient, ingredients):
    if ingredient == 'water':
        ingredients[ingredient] = 300
        print(ingredients[ingredient])
    elif ingredient == 'milk':
        ingredients[ingredient] = 200
    else:
        ingredients[ingredient] = 100
    return ingredients

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.00
keep_going = True

while keep_going:
    drink = input("What would you like to drink? espresso, latte, cappuccino?").lower()
    if drink == "report":
        print(f'water: {resources["water"]} ml\nmilk: {resources["milk"]} ml\ncoffee: {resources["coffee"]} g\nmoney: '
              f'${money:.2f}')
    elif drink == "off":
        keep_going = False
    else:
        order = make_drink(drink, resources)
        if order == 'water' or order == 'milk' or order == 'coffee':
            refill = input(f"Add more {order}? Type y or n").lower()
            if refill == 'y':
                add_ingredients(order, resources)
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            entered_cash = calc_money(quarters, dimes, nickels, pennies, drink)
            change = calc_change(entered_cash, MENU[drink]["cost"])
            if change < 0:
                print("Not enough money, away from this machine peasant!")
                unmake_drink(drink, resources)
            else:
                print(f"Here is ${change:.2f} in change.\nHere is your {drink}. Enjoy!")
                money += entered_cash - change

