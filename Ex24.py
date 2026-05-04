
def horizontal():
    print('-' * size)
    return

def vertical():
    print('|' * size)
    return




size = int(input("How big do you want the Tic Tac Toe game be: "))


for item in range(size):
    horizontal()
    vertical()
    if item == size-1:
        horizontal()





















