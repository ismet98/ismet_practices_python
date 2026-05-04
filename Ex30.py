
import random




file = open ('SOWPODS.txt', 'r')
line = file.readline()



Words = []
Jack =[]

for line in file:
    Jack.append(line.strip())

while line:
    Words.append(line.strip())
    line = file.readline()
    

random_word = random.choice(Words)

print(Jack)

print(random_word)


## line.strip() removes any leading or trailing whitespace
## This one reads each line y it is 

## readline() --> Reads a line by line 

# goes to the first line
# we iterate and keep updateing the line we read --> it finds the new line by finding the '\n' character