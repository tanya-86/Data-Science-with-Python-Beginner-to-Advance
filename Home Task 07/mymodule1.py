def region(n):
    list1 = [] #region names
    for i in range(n):
        i = str(input('\nEnter the region name {}: '.format(i+1)))
        list1.append(i)
    return list1

def temp(n):
    list2 = [] #temperature
    for j in range(n):
       j = float(input('\nPlease enter the temperature in degrees Celsius / Fahrenheit {}: '.format(j+1)))
       list2.append(j)
    return list2

def dew_point(n):
    list3 = [] #dew point
    for k in range(n):
        k = float(input('\nPlease enter the Dew Point in degrees Celsius / Fahrenheit {}: '.format(k+1)))
        list3.append(k)
    return list3
    