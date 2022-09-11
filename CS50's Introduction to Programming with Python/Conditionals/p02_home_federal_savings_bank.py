greeting = input().lower()

suffix = 'h'
if 'hello' in greeting:
    print('$0')
elif greeting.endswith(suffix,0,1) and greeting != 'hello':
    print('$20')
elif greeting == 'hello':
    print('$0')

else:
    print('$100')
