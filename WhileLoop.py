correctNumber = 17
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please guess your number : "))
    if userGuess > correctNumber:
        print("Too much")
    elif userGuess < correctNumber:
        print("Too less")
    elif userGuess == correctNumber:
        print("Corrected!!!")
