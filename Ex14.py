


def remove_duplicates(list_1,list_2):
    list_wo_duplicates =[]
    for item in list_1:
        if item not in list_2 and item not in list_wo_duplicates:
            list_wo_duplicates.append(item)
    return list_wo_duplicates

def set_remove_duplicates(list_1,list_2):
    set_wo_dupplicates = set()

    for item in list_1:
        if item not in list_2:
            set_wo_dupplicates.add(item)
    return set_wo_dupplicates
    





a = [1,2,3,4,5]
b = [2,3,4,6]

print(remove_duplicates(a,b))

print(set_remove_duplicates(a,b))




## What did we learn here:

## We learnt about sets --> we can add things --> Sets are things that are only one thing and another thing cannot be added


