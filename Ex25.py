

a = range(0,101)

start_index = a[0]
end_index = a[-1]
guesses = 0


while True:
    number = (start_index + end_index)//2
    guesses += 1
    
    guess = input("Is " +str(number)+ " your number(H,L,Y): ")


    if guess == 'Y':
        print("I am a genius. I managed to do that in " +str(guesses)+ " guesses.")
        break
    elif guess =='H':
        end_index = number
    elif guess =='L':
        start_index = number
