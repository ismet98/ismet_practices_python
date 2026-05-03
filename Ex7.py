

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even =[]

for item in a:
    if item % 2 == 0:
        even.append(item)

print(even)


# b = [number for number in a if number % 2 == 0]
#c = [ number for number in a if number %2 ==0 ]