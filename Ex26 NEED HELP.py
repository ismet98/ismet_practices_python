def check_win(board):
    # horizontal
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # diagonal
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != 0:
        return board[2][0]

    return 0

        


def check_win(list_1):
 
    list_check = [1,2]

    ## Brute force of checking the game
    for item in list_check:
        if list_1[0][0] == item and list_1[0][1] ==item and list_1[0][2] == item:
            return item ## that number has won
        if list_1[0][0] == item and list_1[1][0] ==item and list_1[2][0] == item:
            return item ## that number has won
        if list_1[0][0] == item and list_1[1][1] ==item and list_1[2][2] == item:
            return item ## that number has won
        if list_1[1][0] == item and list_1[1][1] ==item and list_1[1][2] == item:
            return item ## that number has won
        if list_1[2][0] == item and list_1[2][1] ==item and list_1[2][2] == item:
            return item ## that number has won
        if list_1[0][1] == item and list_1[1][1] ==item and list_1[2][1] == item:
            return item ## that number has won
        if list_1[0][2] == item and list_1[1][2] ==item and list_1[2][2] == item:
            return item ## that number has won
        if list_1[2][0] == item and list_1[1][1] ==item and list_1[0][2] == item:
            return item ## that number has won
    
    return 0


    ## Rules --> Can we look down 2 to find one
    ## Rules --> Can we look right 2 to find ont
    ## Rule --> Can we look diagonal right down to find one 
    ## Rule --> Can we look diagonal  right upwards
       

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

number = 0

if number == 0: 
    number = check_horizontal(winner_is_2)
if number == 0:
    number = check_vertical(winner_is_2)
if number == 0:
    number = check_diagonal(winner_is_2)

if number == 1:
    print("1 has won the game.")
elif number == 2:
    print("2 has won the game.")
else:
    print("It is a draw.")
