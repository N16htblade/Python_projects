import os

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

def check_resources(drink_choice, ingredients):
    req_resources = drink_choice["ingredients"]
    for resource in req_resources:        
        if req_resources[resource] > ingredients[resource]:
            print (f"Sorry, not enough {resource}.")
            return False
        else:
            return True


def process_coins(drink):
    cost = drink["cost"]
    print (f"Your drink will be ${cost}.")
    user_total = 0.0
    money = {"quarter": (0.25), "dimes": (0.10), "nickles": (0.05), "pennies": (0.01)}
    
    for coin in money:
        number_coins = int(input(f"how many {coin}?: "))
        user_total += (number_coins * money[coin])
        print (f"Your new total is: ${user_total}")

    if user_total >= cost:
        change = round(user_total - cost, 2)
        if change > 0:
            print (f"Here is ${change} in change.")
        return cost
    else:
        print (f"Sorry, that's not enough money. Money refunded.")
        return 0


cls = lambda: os.system('cls')
cls()
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappucino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print (f"""
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${profit}
        """)
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink, resources):
            profit += process_coins(drink)
            for resource in drink["ingredients"]:
                resources[resource] -= drink["ingredients"][resource]
            print (f"Here is your {choice} ☕. Enjoy!")