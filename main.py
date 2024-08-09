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
    required_water = coffee['ingredients']['water']
    required_milk = coffee['ingredients']['milk']
    required_coffee = coffee['ingredients']['coffee']
    if water < required_water:
        return "Sorry, there is not enough water."
    elif milk < required_milk:
        return "Sorry, there is not enough milk."
    elif coffee < required_coffee:
        return "Sorry, there is not enough coffee."





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
        check_resource(coffee['ingredients'])
