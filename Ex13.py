

def fibo(number):
    
    a=[]
    if number == 1:
        return "1"
    elif number == 2:
        return "1,1"
    else:
        for item in range(number):
            if item ==0:
                a.append(1)
            elif item == 1:
                a.append(1)
            else:
                a.append(a[item-2]+a[item-1])
    
    string = " "
    for item in a:
        if item == a[-1]:
            string = string + str(item)+"."
        else:
            string = string + str(item) + ","
    return string
            

    
    

number = int(input("How many numbers of the Fibonacci series would you like to see: "))

print(fibo(number))
