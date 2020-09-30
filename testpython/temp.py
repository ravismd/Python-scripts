#!/usr/bin/python

def func(temperature):
    if temperature > 25:
        return 'Hot';
    elif temperature >= 15 and temperature <= 25:
        return 'warm'
    elif temperature < 15 and temperature > 0:
        return 'cold'
    else:
        return 'Chilling ----- Tooo cooold '
       
temp = input('Enter the temperature: ')
print(func(temp))


fg = open("file1",'r') 
line = fg.readline()
print(line)
fg.seek(0)
for line in fg:
    if 'line' in line:
        print(line)
