#!/usr/bin/python
import os

isExists = os.system('pgrep dockerd')
if (isExists):
	print("Raviii")

score_theory = 60
score_practical = 20

if(score_theory):
    print("Please check the input score for 'Theory'.") # Step 2.1
elif(score_practical > 50):
    print("Please check the input score for 'Practical'.")  # Step 2.2
else:
    print("Score validated. Your total is: ",score_theory + score_practical) # Ste
