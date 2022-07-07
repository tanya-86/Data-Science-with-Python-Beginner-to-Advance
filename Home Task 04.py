#a)You have deposited 20,000 BDT in the bank for a compound interest of 5% per year. This means, that after one year your balance will
# be your principal + profit. For the next year (the principal + profit)  will be counted as your new principal and profit will be 
# calculated on your new principal. And this will go on. What will be your money after 4 years? [Don’t use the formula C=P(1+r/100)n]
#[Use  in-Place operator]

print("Ans to a:\n")
P = 20000
print('Principal: ', P, 'tk')
P += P*5/100
print('Balance after 1 year: ', P, 'tk')
P += P*5/100
print('Balance after 2 years: ', P, 'tk')
P += P*5/100
print('Balance after 3 years: ', P, 'tk')
P += P*5/100
print('Total balance after 4 years: ', P, 'tk')

#b)Take all the following inputs of a user: Name, Birth year, Nationality, University/College Name, Living Country, Male/Female, and 
# Mobile number (11 digits).
# DO NOT USE ANY IF ELSE or Advance CODE 
# Then, give an output of his/her profile like the following output 👇
# Name: Inputted Name here
# Age: *** years
# Nationality: *** (UPPER CASE)
# University/College: ****
# Current Location: Inputted living country name
# Mobile Number: +8801**********
# Gender: True (if male), False (if female)


print("\nAns to b:\n")
a = input("Name: ")
b = int(input("Birth year: "))
c = input("Nationality: ")
d = input("University/College Name: ")
e = input("Living Country: ")
f = input("Male/Female: ")
g= input('Mobile Number (11 digits): ')

print("\n\nName: ", a)
print("Age: ", 2022 - b, 'years')
print("Nationality: ", c.upper())
print('University/College: ', d)
print('Current Location: ', e)
print('Mobile Number: +88'+ g[0:11]) 
print('Gender: ','male' == f.lower())






