#!/usr/bin/env python3
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program

# Please write a docstring for every function you write.

###############################################################################
# Imports
from random import randint

# Body

def randomInput():
    counter = 0
    randNo = randint(0,26)
    print(randNo)
    while counter <= 5:
        try:
           userInput  = int(input("Guess a integer from 1-25 "))
           if (userInput > randNo):
               print("Too high")
           elif (userInput < randNo):
               print("Too low")
           elif (userInput == randNo):
               print("Correct")
               break
        except ValueError:
            print("You can only enter an integer")

        counter = counter + 1







###############################################################################
def main():
    print("Hello World!")  # Remove this and replace with your function calls
    randomInput()


if __name__ == '__main__':
    main()
