my_string = input('Input: ')

for char in my_string:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(char, end='')
