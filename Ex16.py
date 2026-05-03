
## MUst Bew Uopdated

## Passwords Shoudld be Random, Generate a New Password


## Install a list of random words

## Randomly choose an element of each list

## Add elemets to list

## iteratate through lists and make some upper or lower case

## randomly assign the list 

# that is our string 


import string
import random

a = string.ascii_lowercase
b = string.ascii_uppercase
c = range(0,10)
from string import punctuation
d = list(punctuation)


## this will create equal number of each character
def random_password_generator(number):
    
    password = ""
    for item in range(number):
        if item % 4 == 0:
            password = password + str((random.choice(a)))
        elif item % 4 == 1:
            password = password + str((random.choice(b)))
        elif item % 4 == 2:
            password = password + str((random.choice(c)))
        elif item % 4 == 3:
            password = password + str((random.choice(d)))
    
    ##random.shuffle(password)

    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    return password
    


number = int(input("How many characters long do you want your password to be: "))

password = random_password_generator(number)

print(password)



