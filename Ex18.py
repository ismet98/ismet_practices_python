

import random

def play_game():
    random_number = str(random.randint(1000, 9999))
    while True:
        number_guess = input("Enter a number:")
        cows = 0
        bulls = 0
        
        for i in range(4):
            if number_guess[i] == random_number[i]:
                cows += 1
            elif number_guess[i] in random_number:
                bulls += 1


        
        print(random_number)
        print(cows, "cow", bulls, "bull")
        
        
        if number_guess == random_number:
            print("You've guessed the number," +str(random_number)+ ", correctly")
            break


print("Welcome to the Cows and Bulls Game!")
play_game()