import inflect
p = inflect.engine()


words_list = []


while True:
    try:
        words = input('Name: ').title()
        words_list.append(words)

    except EOFError:
        print()
        break

output = p.join(words_list)
print(f'Adieu, adieu, to {output}')