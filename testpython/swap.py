#!/usr/bin/python
#x = 5
#y = 10

x = input('Enter the number x : ')
#x = input()
y = input('Enter the number y : ')


temp = x
x = y
y = temp


print "value of x after swap = " + str(x)
print "value of y after swap = " + str(y)
