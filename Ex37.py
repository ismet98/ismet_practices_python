

def horizontal(number):
    print("-" * number)

def vertical(number):
    print("|" * number)



number = int(input("Ho big do you want your game to be: "))

for item in range((number)):
    horizontal(number)
    vertical(number)
    if item == number - 1:
        horizontal(number)