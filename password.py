import random


def random_lower():
    lower_list = []
    lower = 'abcdefghijklmnopqrstuvwxyz'
    for i in lower:
        lower_list.append(i)
    random.shuffle(lower_list)

    return lower_list


def random_upper():
    upper_list = []
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in upper:
        upper_list.append(i)
    random.shuffle(upper_list)

    return upper_list


def random_num():
    num_list = []
    n_list = "0123456789"
    for i in n_list:
        num_list.append(i)

    random.shuffle(num_list)
    return num_list


def special_char():
    special_list = []
    special = "!#$%&;()*+,-./:;<=>?@[\]^_`{|}~ \""
    for i in special:
        special_list.append(i)
    random.shuffle(special_list)

    return special_list


your_password = int(
    input('How many characters would you like your password to be? '))

new_list = special_char() + random_num() + random_lower() + random_upper()

final_pass = []
output_password = ''

for i in range(your_password):
    random.shuffle(new_list)
    final_pass.append(new_list[0])

for i in final_pass:
    output_password += i


print(output_password)
