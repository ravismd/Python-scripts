#!/usr/bin/python
import time;  # This is required to include time module.

ticks = time.time()
localtime = time.localtime()
print "Number of ticks since 12:00am, January 1, 1950:", ticks
print "Local Time now is:", localtime

a = [1,2,3,4,5]
for i in a:
	print(" value of i\n" + str(i))
