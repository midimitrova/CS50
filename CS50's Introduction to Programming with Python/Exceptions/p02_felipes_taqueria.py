
items = {
    "Baja Taco": 4,
    "Burrito": 7.5,
    "Bowl": 8.5,
    "Nachos": 11,
    "Quesadilla": 8.5,
    "Super Burrito": 8.5,
    "Super Quesadilla": 9.5,
    "Taco": 3,
    "Tortilla Salad": 8
}

sum = 0


while True:

    try:
        item = input('Item: ').title()
        if item not in items:
            continue

        else:
            if item in items:
                sum += float(items[item])
                print(f'Total: ${sum:.2f}')

    except EOFError:
        print()
        break
