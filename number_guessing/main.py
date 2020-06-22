#################################
# NUMBER GUESSING GAME
#################################

import random

print('***************************************************')
print("NUMBER GUESSING GAME")
print('***************************************************')
print("The System randomly picks a number from 1 - 50 ")
print("User should guess the number")

systemValue = random.randint(0, 10)
runProgram = True

while(runProgram):
    userValue = int(input("Enter Your Guess: "))
    if userValue == systemValue:
        print("Correct Answer")
        runProgram = False
    elif userValue > systemValue:
        print("your value is greater than System value")
    elif userValue < systemValue:
        print("your value is smaller than System value")
