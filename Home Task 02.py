#a)As a CEO of your company, you can have 20% of the company’s profit as your salary per month.
# Last year, from January to April the company purchased 30,000 BDT each month and sold 50,000 BDT products each month. 
# From May to December purchased 20,000 BDT each month and sold out 45,000 BDT products each month. 
# If you calculate your total salary for last year, how much it is?

print('\nMonthly profit per month from January to April:', 50000-30000, 'BDT')
print('His salary per month from January to April:', 20000*(20/100), 'BDT')
print('Total salary from January to April:', 4000*4, 'BDT')

print('\nMonthly profit per month from May to December:', 45000-20000, 'BDT')
print('His salary per month from May to December:', 25000*(20/100), 'BDT')
print('Total salary from May to December:', 5000*8, 'BDT')

print('\nHis total salary for last year:', 16000+40000, 'BDT')



#b)Suppose, Last year in June, Sylhet had a rainfall of 20cm, Chattogram had 40cm, Dhaka 35 cm. But, Bogura had only 20mm.
# If, Sylhet, Chattogram and Dhaka decreased by 5cm of rainfall every next month till October and Bogura increased by 2cm 
# every next month till October, then calculate the total rainfall of each area at the end of October.

print('\n\n\nSylhet:')
print('In June, total rainfall:', 20, 'cm')
print('In July, total rainfall:', 15, 'cm')
print('In August, total rainfall:', 10, 'cm')
print('In September, total rainfall:', 5, 'cm')
print('In October, total rainfall:', 0, 'cm')
print('\nTotal rainfall at the end of October in Sylhet:', 20+15+10+5+0, 'cm')

print('\nChattogram:')
print('In June, total rainfall:', 40, 'cm')
print('In July, total rainfall:', 35, 'cm')
print('In August, total rainfall:', 30, 'cm')
print('In September, total rainfall:', 25, 'cm')
print('In October, total rainfall:', 20, 'cm')
print('\nTotal rainfall at the end of October in Chattogram:', 40+35+30+25+20, 'cm')

print('\nDhaka:')
print('In June, total rainfall:', 35, 'cm')
print('In July, total rainfall:', 30, 'cm')
print('In August, total rainfall:', 25, 'cm')
print('In September, total rainfall:', 20, 'cm')
print('In October, total rainfall:', 15, 'cm')
print('\nTotal rainfall at the end of October in Dhaka:', 35+30+25+20+15, 'cm')

print('\nBogura:')
print('In June, total rainfall:', 2, 'cm')
print('In July, total rainfall:', 4, 'cm')
print('In August, total rainfall:', 6, 'cm')
print('In September, total rainfall:', 8, 'cm')
print('In October, total rainfall:', 10, 'cm')
print('\nTotal rainfall at the end of October in Bogura:', 2+4+6+8+10, 'cm')



#c)Some bricks of 12cm (Length), 6cm (Width), and 2cm (height) size is used to build a wall of 100m2 Area.
#  How many full bricks can be used to build the wall? (Hint: brick area = length x width)
print('\n\n\nBrick_length:', 0.12, 'm')
print('Brick_width:', 0.06, 'm')
print('Brick_area:', 0.12*0.06, 'm2')
print('Total number of full bricks to build the wall:', int(100//(0.12*0.06)))