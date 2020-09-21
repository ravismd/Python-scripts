#!/usr/bin/python

class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def bark(self):
		print(self.name + " is barking yell out  Bow Bow--\n") 

	def doginfo(self):
		print(self.name + " is " + str(self.age) + " years old----\n")

doggy = Dog("Pintu", 5)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)
doggy.doginfo()
skippy.doginfo()
filou.doginfo()
