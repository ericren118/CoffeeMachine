MENU = {
    "expresso": {
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

QUARTERS = 0.25
DIMES = 0.10
NICKLE = 0.05
PENNIE = 0.01

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(current_resources, current_profit):
    """Check the Coffee machine status"""
    print(f'Coffee Machine status:\n Water: {current_resources["water"]}ml \n Milk: {current_resources["milk"]}ml \n '
          f'Coffee: {current_resources["coffee"]}g \n Money: ${"%.2f" % round(current_profit, 2)}')


def check_resources(drink, current_resources):
    """Check if there is enough resources for the order"""
    drink_standard = MENU[drink]["ingredients"]
    warning_message = ""
    if drink in MENU:
        if current_resources["water"] < drink_standard["water"]:
            warning_message = f"Not enough water for a {drink} \n"
        if drink != "expresso":
            if current_resources["milk"] < drink_standard["milk"]:
                warning_message += f"Not enough milk for a {drink} \n"
        if current_resources["coffee"] < drink_standard["coffee"]:
            warning_message += f"Not enough coffee beans for a {drink}"
    else:
        warning_message = "Please check your drink choice!"
    if warning_message != "":
        print(warning_message)
        resource_available = False
    else:
        resource_available = True
    return resource_available


def make_coffee(ordered_drink, current_resources):
    """Reduce resources and update profit"""
    ingredients = MENU[ordered_drink]["ingredients"]
    for ingredient in ingredients:
        current_resources[ingredient] -= ingredients[ingredient]

    print("Here is your ☕. Enjoy!")


def payment(drink, current_profit):
    """return boolean value for payment status and current profit"""
    quarter_num = int(input("How many quarters? "))
    dime_num = int(input("How many dimes? "))
    nickle_num = int(input("How many nickles? "))
    pennie_num = int(input("How many pennies? "))

    total_payment = QUARTERS * quarter_num + DIMES * dime_num + NICKLE * nickle_num + PENNIE * pennie_num
    drink_price = MENU[drink]["cost"]

    if total_payment < drink_price:
        print(f"Sorry, that's not enough money for a ${drink_price} {drink} \n"
              f"Your payment of {total_payment} has been refunded.")
        payment_successful = False
        return payment_successful, current_profit
    else:
        if total_payment > drink_price:
            change = '{:.2f}'.format(round(total_payment - drink_price, 2))
            print(f"Here is ${change} dollars in change.")
        current_profit += drink_price
        payment_successful = True
        return payment_successful, current_profit


def start_coffee_machine():
    current_profit = profit

    machine_on = True
    while machine_on:
        drink = input("What would you like? expresso/latte/cappuccino: ").lower()
        if drink == "report":
            print_report(resources, current_profit)
        elif drink == "off":
            print("Turning off...")
            machine_on = False
        else:
            if check_resources(drink, resources):
                payment_status, current_profit = payment(drink, current_profit)
                if payment_status:
                    make_coffee(drink, resources)


start_coffee_machine()
