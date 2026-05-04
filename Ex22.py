


words ={}

with open('Ismet.Ozer.txt', 'r') as open_file:
    all_text = open_file.read() ## this is how we open a file

    
for item in all_text:
    if item not in words:
        words[item] =1
    if item in words:
        words[item] +=1

print(words)


## How to Use a DIctionary

## dictionary ={{}}
## dictionary [word] = 1  ## sets the relation between word and dictionary 