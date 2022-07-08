#Description: Use the Github initial code named mymodule2.py. It has some data sets of popular Instagram users with
# their names, followers, designations, and countries. Your Program is basically a game, which shows us details of 2
# Instagram users from the data set except the follower data. The Gameplayer must guess which person's follower number
# is higher. If the Player is correct, add 5 points and continue the game. If answered wrong, the game will end and
# show the total score.

print("Ans to Q:\n")

print("""
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/
""")

print("""
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
""")

print("\nWelcome to the game!")
name = input("What is your name?\n")
print(f"\n{name}, you have to find the Instagram user with higher number of followes!!\nLet's start!")

import random
import mymodule2

data1 = mymodule2.list()
a = len(data1)
point = 0

for i in range (a):
    r = [random.choice(data1) for j in range(2)]
    b = r[0]['follower_count']
    c = r[1]['follower_count']
    del (r[0]['follower_count'], r[1]['follower_count'])

    print("\nThe two Instagram users are:\n", r)
    print('\nGuess which ID has more followers!')
    name1 = input("Please enter the name: ")

    if (b > c) and name1 == r[0]['name']:
        print('Correct! You have got 5 points!')
        point = point + 5
        print('Total point be: ', point)
    elif (b < c) and name1 == r[1]['name']:
        print('Correct! You have got 5 points!')
        point = point + 5
        print('Total point be: ', point)
    else:
        print('\nWrong! The end!')
        print('Total point be: ', point)
        break



