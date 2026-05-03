
import random


def element_search(list_1, number):
    start_index = 0
    end_index = len(list_1) - 1

    if number < list_1 [start_index]:
        return False
    if number > list_1 [start_index]:
        return False

    while True:
        index = (start_index + end_index)//2
        if number == list_1[index]:
            return True
        elif number > list_1[index]:
            start_index = index
        elif number < list_1[index]:
            end_index = index
        else:
            return False
 
a = [1,2,4,5,6]
b = int(input("Please insert an nnumber here: "))

print(element_search(a,b))

