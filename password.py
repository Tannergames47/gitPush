import random


your_password = int(input("How many characters would you like your password to be? "))
output_password = ""
digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%+/:=?@_"

for i in range(your_password):
    save = random.choice(digits)
    output_password += save

print(output_password)
