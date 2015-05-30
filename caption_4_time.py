import time
import calendar
import datetime

print time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))

print calendar.HTMLCalendar(2008).formatweekheader()
print dir(calendar)

d1= datetime.datetime.now()
d2= datetime.datetime(2015, 2, 16)

print (d2-d1).days
print (d2-d1).seconds

print d2-datetime.timedelta(1)

def function():
    print "function!"
    return


function()


# str = raw_input("Enter your input: ");
# print "Received input is : ", str
