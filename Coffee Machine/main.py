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

profit = 0


def is_resources_sufficient(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def check_transaction(drink_cost, amount_money):
    if drink_cost > amount_money:
        print("Sorry not enough money.")
        return False
    elif drink_cost < amount_money:
        change = round(amount_money - drink_cost, 2)
        print(f"Here is your ${change} change.")
        global profit
        profit += drink_cost
        return True


def amount_of_money():
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    sum_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return sum_money


def make_coffee(coffee_name, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {coffee_name} ☕. Enjoy!")


def game():
    is_game = True
    while is_game:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
        if coffee_choice == "off":
            is_game = False
        elif coffee_choice == "report":
            print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:${profit}")
        else:
            drink = MENU[coffee_choice]
            if is_resources_sufficient(drink["ingredients"]):
                sum_money = amount_of_money()
                if check_transaction(drink["cost"], sum_money):
                    make_coffee(coffee_choice, drink["ingredients"])


game()



