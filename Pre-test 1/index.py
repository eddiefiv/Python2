# Q1 - Create a house in ASCII art using print statements
print("----START OF Q1----")
print(
r"""
  ____||____
 ///////////\
///////////  \
|    _    |  |
|[] | | []|[]|
|   | |   |  |
""")

#Q2 - Write a print statement that kicks out any number and string together.
print("----START OF Q2----")
#TODO: Write this

#Q3 Create a program that ask the user to enter their age, and then create an output that multiplies their age by 2
print("----START OF Q3----")
age = input('Please enter your age: ')
print(f'Your age, doubled: {int(age) * 2}')

#Q4 create a menu/list with 3 items, then using an IN statement print out if one of those items exist in the list or not.
print("----START OF Q4----")
list = ['dog', 'cat', 'mouse']

if input('Find in list: ') in list:
    print('Found in list')
else:
    print('Couldnt find in list')

#Q5 take the string “Hello world” and using formatting to print out the string in all caps and as it would be in a book title
print("----START OF Q5----")
string = "Hello world"
print(string.upper())