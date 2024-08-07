from art import logo
from menu import coffee_type
from resource import resource

print(logo)


def report_resource():
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']
    money = resource['money']
    return f"The coffee machine currently has {water}ml of water, {milk}ml of milk, and {coffee}g of coffee."


user_input = input("What would you like? Type 'cappuccino', 'latte', or 'espresso': ")

if user_input == 'report':
    print(f"{report_resource()}")

turn_off = False

while not turn_off:
    if user_input == 'off':
        turn_off = True
        print("Machine turned off.")

