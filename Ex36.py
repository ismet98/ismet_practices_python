import json
import calendar
from bokeh.plotting import figure, show, output_file

with open("scientist_birthdays.json", "r") as file:
    birthday_dict = json.load(file)

list_of_months = list(calendar.month_name)[1:]
count_month_dict = {month: 0 for month in list_of_months}

output_file("output.html")

for name, birthday in birthday_dict.items():
    month_num = birthday[0:2]  # adjust format if needed
    month_name = calendar.month_name[int(month_num)]
    count_month_dict[month_name] += 1

x = list(count_month_dict.keys()) ## must be in list format
y = list(count_month_dict.values())

p = figure(x_range=x)
p.vbar(x=x, top=y, width=0.5)

show(p)

