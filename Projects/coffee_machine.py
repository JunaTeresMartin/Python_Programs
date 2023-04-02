#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that creates a coffee machine program
#DATE     :  02-04-2023

def balance_money(drink):
    #calculates balance money
    one = int(input("How many one rupee coin(s): "))
    two = int(input("How many two rupee coin(s): "))
    five = int(input("How many five rupee coin(s): "))
    ten = int(input("How many ten rupee coin(s): "))
    twenty = int(input("How many twenty rupee coin(s): "))
    sum=1*one+2*two+5*five+10*ten+20*twenty
    drinkIs = MENU[drink]
    cost=drinkIs['cost']
    print(f"Cost of your {drink} is {cost} rupees")
    print(f"Amount you paid= {sum}")
    balance=sum-cost
    if balance>=0:
        make_coffee(choice)
        global profit
        profit += cost
        print(f'Here is {balance} rupees in change')
        print(f"Enjoy your {choice}! Have a nice day.\n")
    else:
        print("Sorry that's not enough money. Money refunded.\n")


def make_coffee(choice):
    #makes coffee and deduce the resources
    drinkIs = MENU[choice]
    ingredients = drinkIs['ingredients']
    for item in ingredients:
        resources[item]-=ingredients[item]

def isSufficientIngredients(ingredients):
    #checks whether there are enough resources
    for item in ingredients:
        if resources[item] <= ingredients[item]:
            print(f"Sorry! There is no enough {item}")
            return False
    return True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 36,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 55,
    }
}

resources = {
    "water": 800,
    "milk": 500,
    "coffee": 300,
}
profit = 0
while(1):
    print("Enter 'report' to get the resources available/'off' to turn off machine")
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == 'report':
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}ml")
        print(f"profit={profit} rupees")
    elif choice == 'off':
        break
    else:
        drinkIs = MENU[choice]
        ingredients = drinkIs['ingredients']
        if isSufficientIngredients(ingredients):
            balance_money(choice)

        else:
            continue
