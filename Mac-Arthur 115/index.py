#TODO: Print details explaining game rules
print("This game will be able to tell your month and age based off your inputs,")
print("assuming it doesn't take note of your inputs as knowledge and uses solely the algorithm to")
print("conclude your name and age. Now follow the prompts to continute.")

#NOTE: ALGORITHM
#Month of birth (Example February): 2
#Double it: 4
#Add 5: 9
#Multiply by 50: 450
#Add friend's age (Example 40): 490
#Subtract 365: 125

#2. Prompt the user for both a birth month (1 for Jan, 2 for Feb etc.) and their age.
#3. Print out the “special” number that results from the algorithm above.
#4. Add 115 to the number, and find the value of the last two digits (age) and the first one or 
#two digits (birth month).
#5. Print out the birth month and the age of the player, explaining to the user what the 
#numbers mean

def algo(inp: int, friend: int) -> int:
    return (((((inp * 2) + 5) * 50) + friend) - 365)

if __name__ == "__main__":
    month = input("Enter your birth month as a numerical value: ")
    age = input("Enter yours or your friends age: ")

    result = algo(int(month), int(age))
    added = result + 115
    added_age = 0
    added_month = 0

    if len(str(added)) == 4:
        added_age = str(added)[-2:]
        added_month = str(added[0:2])
    elif len(str(added)) == 3:
        added_age = str(added)[-2:]
        added_month = str(added)[0:1]

    print(f'Algorithm output ({result}) + 115: {result + 115}')
    print(f"Birth month: {added_month}, age: {added_age}")
    print("This algorithm created an output value that will always have your birth month as the first")
    print("1 or 2 digits of the output, and your age as the last 1, 2, or 3 digits")