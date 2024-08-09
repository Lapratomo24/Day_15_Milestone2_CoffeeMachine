from art import logo
from machine import coffee_type, resource

print(logo)

water = resource['water']
milk = resource['milk']
coffee = resource['coffee']
money = resource['money']


def report_resource():
    print(f"{water}ml of water")
    print(f"{milk}ml of milk")
    print(f"{coffee}g of coffee")
    print(f"Current profit: {money}.")


def check_resource(the_ingredients):
    for item in the_ingredients:
        if the_ingredients[item] >= resource[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def inserted_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    # print(f"You inserted ${round(total, 2)}.")
    return total

def check_transaction(coins):
    if total

turn_off = False

while not turn_off:
    selection = input("What would you like? Type 'cappuccino', 'latte', or 'espresso': ")
    if selection == 'off':
        turn_off = True
        print("Machine turned off.")
    elif selection == 'report':
        report_resource()
    else:
        coffee = coffee_type[selection]
        print(coffee)
        if check_resource(coffee['ingredients']):
            inserted_coins()
            check_transaction()