

def prime(number):
    a = range(2,number-1)
    for item in a:
        if number % item == 0:
            return False
    return True


number = int(input("Please insert a number: "))
check = prime(number)

if check is False:
    print("The number, " +str(number)+", is not prime.")
else:
    print("The number, " +str(number)+", is prime.")
