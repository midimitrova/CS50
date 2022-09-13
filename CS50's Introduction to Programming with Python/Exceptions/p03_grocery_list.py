groceries = {}

while True:

    try:
        item = input().upper()

        if item in groceries:
            groceries[item] += 1

        else:
            groceries[item] = 1

    except EOFError:
        sorted_dict = dict(sorted(groceries.items()))
        for k, v in sorted_dict.items():
            print(f'{v} {k}')
        print()
        break

