import random
import string




print("\n\n")
print("Welcom to the random password generator. \n")

length = int(input("How many characters would you like in your password? "))

# check if user wants upper case letters, validate correct input
upp = False
while not upp:
    user = input("Would you like upper case letters availabel? (y or n) ").lower()
    if user == "y":
        upp = True
    elif user == "n":
        upp = False
        break
    else:
        print("You didn't enter y or n")

# check if user wants lower case letters, validate correct input
low = False
while not low:
    user = input(
        "Would you like lower case letters available? (y or n) ").lower()
    if user == "y":
        low = True
    elif user == "n":
        low = False
        break
    else:
        print("You didn't enter y or n")

# does user want to use numbers, validate correct input
num = False
while not num:
    user = input(
        "Would you like numbers available? (y or n) ").lower()
    if user == "y":
        num = True
    elif user == "n":
        num = False
        break
    else:
        print("You didn't enter y or n")

# does user want to use special characters, validate a correct response
special_char = False
while not special_char:
    user = input(
        "Would you like special characters available? (y or n) ").lower()
    if user == "y":
        special_char = True
    elif user == "n":
        special_char = False
        break
    else:
        print("You didn't enter y or n")

# all the letters imported from string module
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
characters = string.punctuation


print(characters, lower_letters, upper_letters, numbers)

# build a list of all they characters they choose
possible_password = []

# holding tank for the final password
password = ""

if upp == True:
    possible_password.append(upper_letters * length)

if low == True:
    possible_password.append(lower_letters * length)

if num == True:
    possible_password.append(numbers * length)

if special_char == True:
    possible_password.append(characters * length)

lets_see = " ".join(possible_password)

if len(lets_see) == 0:
    print("You didn't choose any valid options. ")
else:
    for i in range(length):
        save = random.choice(lets_see)
        password += save
    
print(f"Your new password is \n {password}")












