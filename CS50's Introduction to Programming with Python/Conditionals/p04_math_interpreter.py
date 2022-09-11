x, y, z = input('Expression: ').split(' ')

x = int(x)
z = int(z)

if y == '+':
    result = x + z
    print(f'{result:.1f}')
elif y == '-':
    result = x - z
    print(f'{result:.1f}')
elif y == '*':
    result = x * z
    print(f'{result:.1f}')
elif y == '/' and z != 0:
    result = x / z
    print(f'{result:.1f}')