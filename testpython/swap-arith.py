#!/usr/bin/python

x = input('Enter the x num:  ')
y = input('Enter the y num:  ')

x, y = y, x
print ("value of x and y are == ", x, y)

x = x + y
y = x - y
x = x - y


print ("value of x and y are == ", x, y)
