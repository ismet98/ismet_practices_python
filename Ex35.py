import json
import calendar

file = open("birthday.json", "r")
birthday_dict = json.load(file)

list_of_months = list(calendar.month_name)[1:]

count_month_dict = {}

for item in list_of_months:
    count_month_dict[item] = 0 ## we put item here --> and for each one we add 0

## print(count_month_dict)

for item in birthday_dict:
    if birthday_dict[item][3:5] == "01":
        count_month_dict["January"] +=1
    if birthday_dict[item][3:5] == "02":
        count_month_dict["February"] +=1
    if birthday_dict[item][3:5] == "03":
        count_month_dict["March"] +=1
    if birthday_dict[item][3:5] == "04":
        count_month_dict["April"] +=1
    if birthday_dict[item][3:5] == "05":
        count_month_dict["May"] +=1
    if birthday_dict[item][3:5] == "06":
        count_month_dict["June"] +=1
    if birthday_dict[item][3:5] == "07":
        count_month_dict["July"] +=1
    if birthday_dict[item][3:5] == "08":
        count_month_dict["August"] +=1
    if birthday_dict[item][3:5] == "09":
        count_month_dict["September"] +=1
    if birthday_dict[item][3:5] == "10":
        count_month_dict["October"] +=1
    if birthday_dict[item][3:5] == "11":
        count_month_dict["November"] +=1
    if birthday_dict[item][3:5] == "12":
        count_month_dict["December"] +=1

display_dict = {} ## only display things which are short

for item in count_month_dict:
    if count_month_dict[item] != 0:
        display_dict[item] = count_month_dict[item]

print(display_dict)





    
    
    
