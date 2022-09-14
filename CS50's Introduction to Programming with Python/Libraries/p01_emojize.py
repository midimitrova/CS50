import emoji

my_emoji = input('Input: ')

output = emoji.emojize(my_emoji, language='alias')

print(f'Output: {output}')