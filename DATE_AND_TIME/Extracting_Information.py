#The first line imports the datetime library so that we can use it.
#The second line will print out the current date and time.
#using . and name of year , month, day we get indivisual values
#We not use now.time we not get any value
from datetime import datetime
now=datetime.now()
print(now.year)
print(now.month)
print(now.day) 
print(now.hour)
print(now.second) 
print(now.minute)
