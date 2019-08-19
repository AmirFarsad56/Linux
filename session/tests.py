from django.test import TestCase


import jdatetime
from jdatetime import date as jdate
now = jdatetime.datetime.now()
if now.month == 12:
    month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
    previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
    this_date = str(now.year)+'-12-'
    next_date = str(now.year+1)+'-1-'
    prev_date = str(now.year)+'-11-'
elif now.month == 1:
    month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
    previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
    this_date = str(now.year)+'-1-'
    next_date = str(now.year)+'-2-'
    prev_date = str(now.year-1)+'-12-'
else:
    month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
    previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
    this_date = str(now.year)+'-'+str(now.month)+'-'
    next_date = str(now.year)+'-'+str(now.month+1)+'-'
    prev_date = str(now.year)+'-'+str(now.month-1)+'-'

first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
print(month_length , first_day_of_month_weekday)
array = [0,]
days = [0,]
if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
    for i in range(41):
        array.append(0)
        days.append(0)
else:
    for i in range(34):
        array.append(0)
        days.append(0)


for i in range(first_day_of_month_weekday):
    array[first_day_of_month_weekday-i-1] = prev_date + str(previous_month_length - i)

for i in range(month_length):
    array[first_day_of_month_weekday+i] = this_date + str(i + 1)

for i in range(len(array) - array.index(0)):
    array[array.index(0)] = next_date+ str(i+1)
print('sssssssssssssssssssssssssss')    
for i in range(len(array)):
    print((int(i/7)+1)*7-1-(i-int(i/7)*7))
