import random


def random_password():
    master_list = []
    lower = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&;()*+,-./:;<=>?@[\]^_`{|}~ \"'
    for i in lower:
        master_list.append(i)
    random.shuffle(master_list)

    return master_list


your_password = int(
    input('How many characters would you like your password to be? '))


output_password = ''
for i in range(your_password):
    save = random_password()
    output_password += save[0]


print(output_password)
