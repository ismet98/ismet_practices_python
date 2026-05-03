
def rock_paper_scissors(player_1,player_2):
    if player_1 == "R" and player_2 == "S":
        return 1 ## player 1 wins
    elif player_1 == "R" and player_2 == "P":
        return 2 ## player 2 wins
    elif player_1 == "R" and player_2 == "R":
        return 0
    elif player_1 == "P" and player_2 == "S":
        return 2 ## player 2 wins
    elif player_1 == "P" and player_2 == "R":
        return 1 ## player 1 wins
    elif player_1 == "P" and player_2 == "P":
        return 0
    elif player_1 == "S" and player_2 == "S":
        return 0
    elif player_1 == "S" and player_2 == "R":
        return 2 ## player 2 wins
    elif player_1 == "S" and player_2 == "P":
        return 1 ## player 1 wins

   
    


while True:
    player_1= input("Please choose rock paper or scissors (R,P,S): ")
    player_2= input("Please choose rock paper or scissors (R,P,S): ")
    winner = rock_paper_scissors(player_1,player_2)
    if winner == 1:
        print("Player 1 won the game!")
        break
    elif winner == 2:
        print("Player 2 won the game!")
        break
    elif winner == 0:
        print("It was a tie! Please try again. \n")
        continue
    else:
        print("Invalid input. Please insert correct letters!\n")
        continue



    



    
