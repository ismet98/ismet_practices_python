


name = input("Please insert a string: ")



for item in range(len(name)):
    if name[item] != name[len(name) - item - 1]:
        print("This string is not a palindrome.")
        break
    if item == len(name) - 1:
        print("This string is a palindrome.")
