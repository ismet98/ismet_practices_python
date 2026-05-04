



## Not DONE


list1 =[]

with open('happy.txt', 'r') as happy_file:
    happy_text = happy_file.read() ## this is how we open a file

with open('prime.txt','r') as prime_file:
    prime_text = prime_file.read()

for item in happy_text:
    if item in prime_text:
        list1.append(item)
    
print(list1)