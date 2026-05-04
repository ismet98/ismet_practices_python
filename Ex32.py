
def random_word():
    import random
    file = open ('SOWPODS.txt', 'r')
    line = file.readline()
    Words = []
    while line:
        Words.append(line.strip())
        line = file.readline()
    word = random.choice(Words)

    return word

def hangman_game(word):

    word_temp = []

    for item in range(len(word)):
        word_temp.append("_")

    result_word_temp = "".join(word_temp)


    number_of_guesses = 6


    incorrect_guessed_letters=[]

    
    while number_of_guesses != -1:
        print(result_word_temp)
        temp_letter = input("Guess your letter: ").upper()
        if temp_letter in word:
            for i in range(len(word)):
                if word[i] == temp_letter:
                    word_temp[i] = word[i]
            result_word_temp = "".join(word_temp)
            print("You have " +str(number_of_guesses)+" guesses left!")
        elif temp_letter not in word: ## will not penalize them for guessing the same letter
            if temp_letter in incorrect_guessed_letters:
                print("You have " +str(number_of_guesses)+" guesses left!")
                continue
            incorrect_guessed_letters.append(temp_letter)
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print("Oh no. You have lost the game. You do not have any guesses left.\n")
                print("The correct word was",word,"!")
                break
            else:
                print("Incorrect. You have " +str(number_of_guesses)+" guesses left!")
        if '_' not in word_temp:
            print("You've guessed the word correctly! Well done")
            break



word = random_word()
while True:
    print("Welcome to Hangman!")
    hangman_game(word)
    game = input("Thank you for playing. Would you like to play again (Y/N): ").upper()

    if game == 'Y':
        continue
    else:
        break






    