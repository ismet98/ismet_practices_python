
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]

for item in a:
    if item < 5:
        b.append(item)

print(b)



#b = [item for item in a if item < 5] 