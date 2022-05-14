# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
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
    print(f'Coffee Machine status:\n Water: {current_resources["water"]}ml \n Mike: {current_resources["milk"]}ml \n '
          f'Coffee: {current_resources["coffee"]} \n Money: ${current_profit}')


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
    drink = MENU[ordered_drink]["ingredients"]
    current_resources["water"] -= drink["water"]
    current_resources["coffee"] -= drink["coffee"]
    if ordered_drink != "expresso":
        current_resources["milk"] -= drink["milk"]
    print("Here is your ☕. Enjoy!")


def payment(drink, current_profit):
    quarter_num = float(input("How many quarters? "))
    dime_num = float(input("How many dimes? "))
    nickle_num = float(input("How many nickles? "))
    pennie_num = float(input("How many pennies? "))

    total_payment = QUARTERS * quarter_num + DIMES * dime_num + NICKLE * nickle_num + PENNIE * pennie_num
    drink_price = MENU[drink]["cost"]

    if total_payment < drink_price:
        print(f"Sorry, that's not enough money for a ${drink_price} {drink} \n"
              f"Your payment of {total_payment} has been refunded.")
        payment_successful = False
        return payment_successful, current_profit
    else:
        if total_payment > drink_price:
            change = total_payment - drink_price
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
