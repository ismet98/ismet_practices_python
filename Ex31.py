
word ="EVAPORATE"

word = ["E","V","A","P","O","R","A","T","E"]

word_temp = []

for item in range(len(word)):
    word_temp.append("_")

result_word_temp = "".join(word_temp)

print("Welcome to Hangman!")




while '_' in word_temp:
    print(result_word_temp)
    temp_letter = input ("Guess your letter: ")
    if temp_letter in word:
        for i in range(len(word)):
            if word[i] == temp_letter:
                word_temp[i] = word[i]
        result_word_temp = "".join(word_temp)
    elif temp_letter not in word:
        print("Incorrect")

    if '-' not in word_temp:
        print("You've guessed the word correctly! Well done")