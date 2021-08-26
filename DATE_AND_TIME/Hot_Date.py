#Print the current date in the form of mm/dd/yyyy

from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d' % (now.month,now.day,now.year))