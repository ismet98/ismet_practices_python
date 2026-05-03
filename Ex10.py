

def lists(a,b,c):
    for item in a:
        if item in b and item not in c:
            c.append(item)





a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

if len(a) >= len(b):
    lists(a,b,c)
else:
    lists(b,a,c)

print(c)

