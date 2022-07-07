#You are making a Relative Humidity Calculator! You will make modules and functions for each part of this Program.

# Q: Make a Program named “YourName’s Weather Forecast”. It will show the user a welcome message. Then asks the User’s name. 
# Then Addressing his name, your program will ask the user about the region you stay in. Then it will ask for the temperature in 
# degrees Celsius, and Dew Point in degrees Celsius. Make the program such, so that the user can compare the Relative Humidity in 
# as many regions as he/she wants. It will show the user, which region has the highest and the lowest Relative Humidity of all inputs. 
# It also should show the sequence from low humidity to high humidity. If the user does not want to compare, he/she can 
# calculate RH for only one region. You can also make the program more user friendly, by taking input from any unit 
# (Celsius or Fahrenheit). 

# বাংলাঃ “YourName’s Weather Forecast” নামে একটি প্রোগ্রাম তৈরি করুন। এটি ব্যবহারকারীকে একটি স্বাগত বার্তা দেখাবে। তারপর ব্যবহারকারীর নাম 
# জিজ্ঞাসা করুন। তারপর তার নাম সম্বোধন করে, আপনার প্রোগ্রাম ব্যবহারকারী যে অঞ্চলে থাকবেন সে সম্পর্কে জিজ্ঞাসা করবে। তারপর এটি ডিগ্রি সেলসিয়াসে 
# তাপমাত্রা, ডিগ্রি সেলসিয়াসে শিশির বিন্দু জিজ্ঞাসা করবে। প্রোগ্রামটি এমনভাবে তৈরি করুন, যাতে ব্যবহারকারী যতগুলি অঞ্চল চান, আপেক্ষিক আর্দ্রতার তুলনা 
# করতে পারেন। এটি ব্যবহারকারীকে দেখাবে, কোন অঞ্চলে সমস্ত ইনপুটগুলির মধ্যে সর্বোচ্চ এবং সর্বনিম্ন আপেক্ষিক আর্দ্রতা রয়েছে৷ এটি কম আর্দ্রতা থেকে উচ্চ 
# আর্দ্রতা পর্যন্ত ক্রম দেখাতে সক্ষম হবে। ব্যবহারকারী যদি তুলনা করতে না চান, তবে তিনি শুধুমাত্র একটি অঞ্চলের জন্য RH গণনা করতে পারেন। আপনি যেকোন 
# ইউনিট (সেলসিয়াস বা ফারেনহাইট) ইনপুট নিয়ে প্রোগ্রামটিকে আরও ব্যবহারকারী বান্ধব করে তুলতে পারেন।

# The formula for Relative Humidity: Given as an attachment 

# Hints to Use exp(): 

# Python number method exp() returns exponential of x: e^x

# Example:

# import math
# math.exp( x )
# print "math.exp(-45.17) : ", math.exp(-45.17)


print("Ans to the Q:\n")
print ("Welcome!")
name = input("What is your name? ")
n = int(input("Please enter the total number of regions: "))

import mymodule1
reg_name = mymodule1.region(n)
print("\n\nThe list of all regions: ", reg_name)

T = mymodule1.temp(n)
print("\n\nThe list of temperatures of all regions: ", T)

DP = mymodule1.dew_point(n)
print("\n\nThe list of Dew Points of all regions: ", DP)

RH = []
import math
for l in range(n):
    a = math.exp((17.625 * DP[l])/(243.04 + DP[l]))
    b = math.exp((17.625 * T[l])/(243.04 + T[l]))
    c = 100 * (a / b) 
    RH. append(c)

print("\n\nThe list of Relative Humidities of all regions: ", RH)

for m in range(n):
    if RH[m] == max(RH):
        print('\n\nThe region with the highest Relative Humidity: ', reg_name[m])
    if RH[m] == min(RH):
        print('\n\nThe region with the lowest Relative Humidity: ', reg_name[m])

RH.sort()
print('\n\nThe sequence from low to high humidity: ',RH)











