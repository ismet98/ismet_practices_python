



import datetime

today_date= datetime.datetime.now()
today_year= today_date.year

## enter name and age

name = input("What is your name? ")
age= int(input("what is your age? "))
number_of_times =int(input("How many times would you like to see this message?"))


year_turning_100 = (100 - age) + today_year


for x in range(number_of_times):
    print(f"You will be 100 years old in {year_turning_100}.\n")





## print message to them that tells then when they will be 100 years old 


## print the number that many times in seperate lines "\n"