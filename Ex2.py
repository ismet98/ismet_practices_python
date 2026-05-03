


num = int(input("Please provide a number for me:"))
check =int(input("Please provide a number for me to divide by:"))

if num % check ==0:
    print("Your number is divisible by " +str(check)+"." )
elif num % check != 0:
    print("Your number is not divisible by " +str(check)+"." )
