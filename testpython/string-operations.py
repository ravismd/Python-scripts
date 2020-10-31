#!/usr/bin/python

def func(name):
    message = "Hi %s" % (name.title())
    return message

name = input("Enter ut name: ")
sirname = input("Enter ut sirname: ")
#message = "Hello %s %s!" % (name.title(), sirname.title())
print("Hello %s %s!" % (name.title(), sirname.title()))

print(func("Mary"))
