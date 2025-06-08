import random

randNum = random.randint(1, 10)
num = int(input("Guess a number between 1 and 10: "))

while num != randNum: 
    if num > randNum:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    num = int(input("Try again: "))  

print("You guessed it right!") 
