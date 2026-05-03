


number = int(input("Please insert a number: "))

list_of_numbers = range(1,number+1)
list_of_divsors = []


for item in list_of_numbers:
    if number % item == 0:
        list_of_divsors.append(item)
        print(item)

print(list_of_divsors)

