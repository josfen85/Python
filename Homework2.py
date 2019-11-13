from datetime import datetime
from dateutil import relativedelta


Year = int(input("Enter your year: ") )
Month = int(input("Enter your Month in number (Ex:Feb = 2) : "))
Day = int(input("Enter your Day in number : "))


##  Feb 4 1985 8:10 pm
dob = datetime(Year, Month, Day, 20, 10)

##  Now
date_2 = datetime.now()

#  This will find the difference between the two dates
difference = relativedelta.relativedelta(date_2, dob)
daysdiff = (date_2 - dob).days

years = difference.years
months = difference.months
days = difference.days
#  hours = difference.hours
#  minutes = difference.minutes

print('I have been in this world for {} years'.format(years))
print('I have been in this world for {} months'.format(years*12+months))

print('I have been in this world for {} days'.format(daysdiff))

output = ''

for x in range(years):
    output = output + '* '

print(output)

#  Eligible for driving?
if years >= 18:
    print('You can drive')
else:
    print('You are too young to drive')
