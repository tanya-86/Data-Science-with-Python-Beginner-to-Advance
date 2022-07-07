#Q. Description: You are writing a python programming code for a coffee vending machine. The Machine can have a
# limited amount of Water, Sugar, Milk and Coffee Powder. There are three menus and each of the menus needs a separate amount
# of Sugar, Milk, Coffee and Water. When each user came, the machine will be full, but for one run the machine can calculate
# how many types of coffee it can make with its stocked materials. Moreover, it can calculate the Money, Profit, and gives money
# changes to the user.

print("Ans to the Q:\n")

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
print ("Welcome!")
name = str(input("May I take your order? We have espresso, latte and cappuccino."))

list=['espresso', 'latte', 'cappuccino']

for i in range(len(list)):
    if name==list[i]:
        a = MENU[name]['cost']
        print('That will be',a ,'dollars.')
        money = float(input('You gave me: '))
        if money < a:
                print('\nYou need to pay', a - money, 'dollars more. Thank you! Have a nice day!')
        elif money == a:
                print('\nThank you! Have a nice day!')
        elif money > a:
                print('\nHere is your', money - a, 'dollars change. Have a nice day!')
        profit = a
        print('Your profit:', profit)

        rem_water = resources['water'] - MENU[name]['ingredients']['water']
        rem_milk = resources['milk'] - MENU[name]['ingredients'].get('milk',0)
        rem_coffee = resources['coffee'] - MENU[name]['ingredients']['coffee']

        if rem_water >= 250 and rem_milk >= 150 and rem_coffee >= 24:
            print("You can take another cup of Latte or Cappucino.")
        elif rem_water >= 250 and rem_milk >= 100 and rem_coffee >= 24:
            print("You can take another cup of Cappucino.")
        elif rem_water >= 200 and rem_milk >= 150 and rem_coffee >= 24:
            print("You can take another cup of Latte.")
        elif rem_water >= 50 and rem_coffee >= 18:
            print("You can take another cup of Espresso.")







