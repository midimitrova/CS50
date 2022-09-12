s = input('camelCase: ')

for char in s:
    if char.isupper():
        char = char.lower()
        print('_', end="")
    print(char, end='')