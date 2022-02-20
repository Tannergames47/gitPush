import random
import string



def upper():
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
    return upp

def lower():
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
    return low

def number ():
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
    return num

def special_char():
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
    return special_char



print("\n\n")
print("Welcom to the random password generator. \n")

length = int(input("How many characters would you like in your password? "))

upper()
lower()
number()
special_char()


# all the letters imported from string module
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
characters = string.punctuation


possible_password = []
password = ""

if upper:
    possible_password.append(upper_letters * length)
if lower:
    possible_password.append(lower_letters * length)
if number:
    possible_password.append(numbers * length)
if special_char:
    possible_password.append(characters * length)

lets_see = " ".join(possible_password)

if len(lets_see) == 0:
    print("You didn't choose any valid options. ")
else:
    for i in range(length):
        save = random.choice(lets_see)
        password += save
        password.replace(" ","")
    
print(f"Your new password is \n {password}")












