

import json

file = open("birthday.json",'r')
birthday_dict = json.load(file)



print("Welcome to the birthday dictionary. We know the birthdays of: ")

for item in birthday_dict:
    print(item)

lookup = input("Whos birthday do you want to look up: ").upper()

found = False


for item in birthday_dict:
    if item.upper() == lookup:
        print(birthday_dict[item])
        found = True
        break

if found == False:
    print("He/she is unfortunately not here.")