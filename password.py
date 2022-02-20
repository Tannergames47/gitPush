import random
import string


lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
all_letters = string.ascii_letters
numbers = string.digits
characters = string.punctuation
kit_and_kabootal = all_letters + numbers + characters


# must contain at least one upper and one lower character
# must have at least one number and one special character
# minimum length = 10

print("\n\n")
print("Welcom to the random password generator. \n")

length = input("How many characters would you like in your password? ")

# check if user wants upper case letters, validate correct input
# store the answer in variable upp
upp = False
while not upp:
    user = input("Would you like to use any upper case letters? (y or n) ").lower()
    if user == "y":
        upp = True
    elif user == "n":
        upp = False
        break
    else:
        print("You didn't enter y or n")

# check if user wants lower case letters, validate correct input
# store the answer in variable low
low = False
while not low:
    user = input("Would you like to use any lower case letters? (y or n) ").lower()
    if user == "y":
        upp = True
    elif user == "n":
        upp = False
        break
    else:
        print("You didn't enter y or n")

# does user want to use numbers, validate correct input
# store teh answer in varialbe num
num = False
while not num:
    user = input("Would you like to use any lower case letters? (y or n) ").lower()
    if user == "y":
        upp = True
    elif user == "n":
        upp = False
        break
    else:
        print("You didn't enter y or n")

print(upp, low, num)

# car = input("Would you like to use special characters in your password? ( y or n) ")


# your_password = int(input("How many characters would you like your password to be? "))
# output_password = ""
# digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%+/:=?@_"

# for i in range(your_password):
#     save = random.choice(digits)
#     output_password += save

# print(output_password)
