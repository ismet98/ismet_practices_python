


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

def random_password_generator(number):
    password = ""
    

    for item in range(number):
        temp =[]
        temp.append(random.choice(a))
        temp.append(random.choice(b))
        temp.append(random.choice(c))
        temp.append(random.choice(d))
        password = password + str((random.choice(temp)))
    
    return password




number = int(input("How many characters long do you want your password to be: "))
print(random_password_generator(number))



