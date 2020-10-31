#!/usr/bin/python
## initializing the string
temp = "Enter the string"
## splitting the string on space
words = temp.split()
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
print(" ".join(words))
