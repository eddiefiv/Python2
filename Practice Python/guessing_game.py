import random

from enum import Enum

class Returns(Enum):
    TOO_HIGH = (False, "Guess was too high, try lower")
    TOO_LOW = (False, "Guess was too low, try higher")
    CORRECT = (True, "You guessed correct!")

def checkGuess(guess):
    secret = random.randint(1, 100)

    try:
        if int(guess) > secret:
            return Returns.TOO_HIGH
        elif int(guess) < secret:
            return Returns.TOO_LOW
        elif int(guess) == secret:
            return Returns.CORRECT
    except:
        pass

    if guess == "exit":
        print("Quitting...")
        quit()
    else:
        print("No valid responses, quitting...")
        quit()

if __name__ == "__main__":
    correct = False
    while not correct:
        guess = checkGuess(input("Guess a number: "))

        if guess.value[0] == False:
            print(guess.value[1])
        elif guess.value[0] == True:
            print(guess.value[1])
            correct = True