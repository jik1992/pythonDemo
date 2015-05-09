import time
import calendar
import datetime


print time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))

print calendar.HTMLCalendar(2008).formatweekheader()
print dir(calendar)

def function():
    print "function!"
    return


function()


str = raw_input("Enter your input: ");
print "Received input is : ", str


