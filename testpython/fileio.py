#!/usr/bin/python

#when exception is thrown immediately gone to finally block and then next higher exceptions blocks
try:
   fd = open("testfile", "w")
   try:
      fd.write("This is my test file")
   finally:
      print "File open error \n"
except IOError:
	print "Error: cant open the file you bugger check it properly--"
else:
	print "written the content in file succesfully\n"

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      #fh.close()
except IOError:
   print "Error: can\'t find file or read data"

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
print(temp_convert("xyz"));	
