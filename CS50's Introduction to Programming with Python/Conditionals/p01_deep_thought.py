answer = input('What is the answer to the Great Question of life, the Universe and Everything? ')

if answer.strip() == '42':
    print('Yes')
elif answer.lower().strip() == 'forty-two':
    print('Yes')
elif answer.lower().strip() == 'forty two':
    print('Yes')
else:
    print('No')
