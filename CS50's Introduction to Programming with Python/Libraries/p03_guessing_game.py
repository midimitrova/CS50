import random

guess_number = random.randint(1, 100)


while True:
    number = input('Level: ')

    if not number.isdigit():
        continue

    number = int(number)

    if number < 0:
        continue
    elif number > 0:
        find_num = input('Guess: ')
        if not find_num.isdigit():
            continue
        find_num = int(find_num)
        if find_num < 0:
            continue
        elif find_num < guess_number:
            print('Too small!')
        elif find_num > guess_number:
            print('Too large!')
        else:
            print('Just right!')
            break


