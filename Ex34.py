

import json

birthday_dict = birthday_dict={"Ismet Ozer": "27/05/2002", "Fatih Ozer" : "21,09,1999", "Metin Ozer" : "01/07/2010"}

file = open("birthday.json","w")
json.dump(birthday_dict,file)