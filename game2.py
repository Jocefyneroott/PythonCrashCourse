'''
All Cases

USER            COMP            WIN             WINNER
ROCK      -     PAPER    -->   PAPER    -->      COMP
PAPER     -     SCISSORS -->   SCISSORS -->      COMP
SCISSORS  -     ROCK     -->   ROCK     -->      COMP
ROCK      -     SCISSORS -->   ROCK     -->      USER
PAPER     -     ROCK     -->   PAPER    -->      USER
SCISSORS  -     PAPER    -->   SCISSORS -->      USER
'''


# 1 -> rock 
# 2 -> paper 
# 3 -> scissors

import random
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)


print("Press 1 for rock, 2 for paper and 3 for scissors")
def game():
    computer = random.randint(1,3)
    # print(computer) # For Debug
    userInput = int(input("Your Chance: "))
    global userScore
    global computerScore
    if (userInput>0 and userInput<=3):
        if userInput==computer:
            print("Game Draw")
            print("Computer Choose: ", computer)
        elif(userInput==1 and computer==3)or(userInput==2 and computer==1)or(userInput==3 and computer==2):
            print("Computer Choose: ", computer)
            print("You Win!")
            computerScore+=1
        else:
            print("Computer Choose: ", computer)
            print("Computer Win!")
            computerScore+=1
    else:
        logging.warning("Enter 1, 2 and 3 only")


userScore = 0
computerScore = 0
chances = 10
while chances:
    try:
        game()
        chances-=1
        print(f"\t\t\t\t\t\t\t\t[Live:{chances}]")
    except Exception as e:
        logging.warning("Enter 1, 2, and 3 only")

if userScore==computerScore:
    print("******* Game Draw *******")
elif userScore>computerScore:
    print("******* You Win this game *******")
else:
    print("******* Computer Win this game *******")

print("Computer Score: ", computerScore)
print("User Score: ", userScore)