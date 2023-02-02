from enum import Enum

#1 Create a program called checkGuess() with one parameter for the guess. You will need a variable for a secret number inside the function. If the guess is greater than the secretNumber then you need to return a string saying it’s too high. If the guess is less than the secretNumber return too low. If the guess is the same as the secretNumber, return a string congratulating the user.
class Returns(Enum):
    TOO_HIGH = (False, "Guess was too high, try lower")
    TOO_LOW = (False, "Guess was too low, try higher")
    CORRECT = (True, "You guessed correct!")

def checkGuess(guess):
    secret = 56

    if int(guess) > secret:
        return Returns.TOO_HIGH
    elif int(guess) < secret:
        return Returns.TOO_LOW
    elif int(guess) == secret:
        return Returns.CORRECT

#2 Create a program called iceCream() with two parameters for flavor and number of scoops. The program should use if, elif and else to display the following output.
def iceCream(flavor: str, scoops: int):
    if flavor.lower() == "chocolate":
        print(f"Chocolate is my favorite too. You are getting {scoops} scoops.")
    elif flavor.lower() == "strawberry":
        print(f"You are getting {scoops} scoops of Strawberry. Sweet!")
    elif flavor.lower() == "vanilla":
        print(f"Vanilla is awesome! You are getting {scoops} scoops.")
    else:
        print(f"You would like {scoops} scoops of {flavor}.")

# Main
if __name__ == "__main__":
    correct = False
    while not correct:
        guess = checkGuess(input("Guess a number: "))

        if guess.value[0] == False:
            print(guess.value[1])
        elif guess.value[0] == True:
            print(guess.value[1])
            correct = True

    iceCream(input("What flavor do you want: "), input("How many scoops: "))