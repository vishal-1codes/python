#Print the date and time together in the form: mm/dd/yyyy hh:mm:ss
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month,now.day,now.year,now.hour, now.minute, now.second))