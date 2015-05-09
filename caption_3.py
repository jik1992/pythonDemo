# coding=utf-8
# !/usr/bin/python


# wait output \n
# raw_input ("\nPress the enter key to exit.")

import random

total = 1 + \
        2 + \
        3

if total > 0:
    print(total)
elif total == 0:
    print("equal 0")
else:
    print("error")

num = 1
doubleNum = 1.1

# delete object
del num

str = "hello world"
print str[0:5]

# java list
list = ["12", "asd", "111"]
if ("12" in list):
    print(True)
if ("11" not in list):
    print(False)
del list[2]

# list but only read
tuple = (1, 231, "fa")
# dict
dict = {'name': "zuoyun", "sex": "man"}
print(dict)

# convert
print hex(111)
print int(1.1)
print long(111)
# print str("xxx")
print ord("a")

# operator
print 2 ** 3  # ^
print 12 // 4  # division

# == is    meaning like javasctipt
a = 20
b = 20
if id(a) == id(b):
    print("a value equal b vaule")
b=30
if a is not b:
    print "a object not is b object"

print random.choice(range(10))

print '''
what you see is what you get
≈çå≈ççßå´∑ƒ√≈ßßßßß

'''

print u'我是中文'

i=0
while i<10:
    ++i

for i in "hello world":
    print i+"\t"

