#Question 01: Write a program that switches the values stored in the variables a and b. Your program should work for different inputs.
#  e.g. any value of a and b.
# 🚨 Don't change the code below 👇
#a = input("a: ")
#b = input("b: ")
# 🚨 Don't change the code above 👆
###################################
#Write your code below this line 👇
#Write your code above this line 👆
##################################
#🚨 Don't change the code below 👇
#print("a: " + a)
#print("b: " + b)

print("Ans to 1:\n")
a = input("a: ")
b = input("b: ")
temp = a
a = b
b = temp
print("a: " + a)
print("b: " + b)

#Question 02: There are errors in all of the lines of code. Fix the code so that it runs without errors.
# The output in your program should match the example output shown below exactly, character for character, even spaces and symbols 
# should be identical, otherwise, the tests won't pass. 
#When you run your program, it should print the following:
#Your Output should be exactly like the below 👇
#Day 1 - String Manipulation
#String Concatenation is done with the "+" sign.
#e.g. print("Hello " + "world")
#New lines can be created with a backslash and n.
#Your Output should be exactly like the above 👆
#Fix the code below 👇
#print(Day 1-String Manipulation")
#print('String Concatenation is done with the ‘+’ sign.’)
#e.g. print(Hello + world)
#print(New lines can be created with a backslash and n.")
#Fix the code above 👆

print("\nAns to 2:\n")
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#Question 03: Kitty sent a message with EID Mubarak to her 40 friends on Facebook. Half of them did not even do seen the message. 
# Of the seen messages, half of them again forwarded the message to 10 of their friends. How many people got the EID Mubarak message, 
# keep your answer in the variable named MSG_got.

print("\nAns to 3:\n")
MSG_sent = 40
MSG_seen = 20
MSG_forwarded = 10 * 10
MSG_got = MSG_sent + MSG_forwarded
print('Total number of people who got the EID Mubarak message:', MSG_got)

#Question 04: What will be the value of a? 
#2 + 3 + 5 + 8 + 13 + a
#use maximum 2 variables to solve this. Keep the answer in variable a. 

print("\nAns to 4:\n")
a = 8
b = 13
a = a + b
print('The value of a is:', a)

#Question 05: Write a code that can give you a total or summation from a to b.
#Suppose,
#a = 10
#b = 90
#Keep the answer in the variable named SUM.
#Hint: use formula for the following 10+11+12+…….+88+89+90 = ?

print("\nAns to 5:\n")
a = 10
b = 90 
#n : total number of terms
n = (90 - 10) + 1
SUM = (n/2) * (a + b)
print("The total summation from 10 to 90:", SUM)

