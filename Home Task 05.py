#1. Make a code that will take the input of two strings. If the two inputs are the same, your program will print “SAME”.
# If Not, It should show “NOT Same” and check which one is greater and print that.

print("Ans to 1:\n")
a  = str(input('Enter the 1st string: '))
b = str(input('Enter the 2nd string: '))
if a == b:
    print("\nSAME")
else: 
    print("\nNOT Same")
    if a > b:
        print('Greater string is: ',a)
    else:
        print('Greater string is: ',b)

#2. Make a calculator, which will work as the following algorithm: 
# a.Input 1st Number
# b.Input What you want to do with numbers (+, -, *, or /)
# c.Input 2nd Number
# d.Do calculation 
# e.Show Result

print("\nAns to 2:\n")

num_1 = float(input('Enter the 1st number: '))
operation = input('Enter the operation: ')
num_2 = float(input('Enter the 2nd number: '))

if operation == '+':
    print('num_1 + num_2 = ', num_1 + num_2)
elif operation == '-':
    print('num_1 - num_2 = ', num_1 - num_2)
elif operation == '*':
    print('num_1 * num_2 = ', num_1 * num_2)
elif operation == '/' and num_2 != 0:
    print('num_1 / num_2 = ', num_1 / num_2)
else:
    print('Error!')

#3.Rainfall = [22, 3.4, 1, 8, 19, 21]
#From the above rainfall data, Find the average rainfall of that area.

print("\nAns to 3:\n")
Rainfall = [22, 3.4, 1, 8, 19, 21]
avg_rainfall = (Rainfall[0]+ Rainfall[1] + Rainfall[2] + Rainfall[3] + Rainfall[4] + Rainfall[5])/6
print('Average rainfall of that area: ', avg_rainfall)

#4. A school has the following rules for the grading system:
#   a. Below 25 - F
#   b. 25 to 45 - E
#   c. 45 to 50 - D
#   d. 50 to 60 - C
#   e. 60 to 80 - B
#   f. Above 80 – A
# Ask the user to enter marks and print the corresponding grade.

print("\nAns to 4:\n")

a = float(input('Please enter your marks: '))

if a < 25:
    print('Grade: F!')
elif a >= 25 and a  < 45: #25 <= a < 45
    print('Grade: E!')
elif a >= 45 and a  < 50:
    print('Grade: D!')
elif a >= 50 and a  < 60:
    print('Grade: C!')
elif a >= 60 and a  < 80:
    print('Grade: B!')
else:
    print('Grade: A!')





