


def reverse_order(ordered_string):
    reverse_order_string = ""
    for item in range(len(ordered_string)):
        reverse_order_string = reverse_order_string + ordered_string[len(ordered_string)-item - 1]
    
    return reverse_order_string

def reverse(ordeered_string):
    return ordered_string[::-1]


ordered_string = input("Please insert a string here: ")

print(reverse_order(ordered_string))
print(reverse(ordered_string))
print(ordered_string)