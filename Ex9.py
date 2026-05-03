

import random

a= random.randint(1,9)
count = 0

while True:
    guess = int(input("I'm thinking of a number! Can you guess it: "))
    count = count + 1


    if guess > a:
        print("Too high!")
        continue
    if guess < a:
        print("Too low!")
        continue
    if guess == a:
        print("You got it! You got it in "+ str(count)+ " tries")
        break
    