import random

compGuess = random.randint(1,100)
# print(compGuess)

userScore = 0
while True:
    userGuess = int(input("Choose a Number between (1, 100): "))

    if (userGuess>100 or userGuess<1):
        print("Enter Number Between 1 to 100")
    elif compGuess==userGuess:
        print("****** Correct Guess ******")
        print(f"You take {userScore} chances to Guess Correct One")
        print("Computer GUess:", compGuess)
        break
    elif userGuess>compGuess:
        print("Lower Number Please")
        userScore+=1
    elif userGuess<compGuess:
        print("Higher Number Please")
        userScore+=1
