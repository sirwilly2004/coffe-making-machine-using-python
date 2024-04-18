import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
        "tip_percentage": 0.20
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
        "tip_percentage": 0.40
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
        "tip_percentage": 0.50
    }
}

sale = 0
cost = 0
total_tip = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return total calculated from coins inserted."""
    try:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.10
        nickles = int(input("how many nickles?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01
        return quarters + dimes + nickles + pennies
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return process_coins()


def is_transaction_successful(payment, cost):
    """Return True if payment is accepted, False if insufficient."""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global sale
        sale += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


def calculate_tip(total_bill):
    """Calculate tip based on the total bill."""
    try:
        tip_percentage = float(input("How much tip would you like to give? (10, 12, or 15): "))
        if tip_percentage not in [10, 12, 15]:
            raise ValueError("Invalid tip percentage.")
        tip_amount = total_bill * (tip_percentage / 100)
        print(f"The tip amount is ${tip_amount:.2f}.")
        return tip_amount
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid tip percentage.")
        return calculate_tip(total_bill)


def report():
    """Print the available resources and total sales."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${sale:.2f}")
    print(f"Total Tip: ${total_tip:.2f}")


def coffee_maker():
    """Main function to run the coffee maker game."""
    print("Welcome to the Coffee Making Game!")
    time.sleep(1)

    print("\nYou are at the coffee station. Let's make your perfect cup of coffee.")
    time.sleep(1)

    while True:
        choice = input("\nChoose the type of coffee you want to make (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
                    global total_tip
                    total_tip += calculate_tip(drink["cost"])
                    print("Thanks for patronizing use")
        else:
            print("Invalid choice. Please choose a valid option.")


# Run the coffee maker game
coffee_maker()
