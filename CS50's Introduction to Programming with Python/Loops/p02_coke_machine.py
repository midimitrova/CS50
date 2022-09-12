amount_due = 50
total_coins = 0

while True:
    coins = int(input('Insert coins! '))
    if coins not in [25, 10, 5]:
        print(f'Amount due: {amount_due}')

        amount_due = 50
        total_coins = 0
        continue
    amount_due -= coins

    total_coins += coins
    change = amount_due

    if change == 0:
        print(f'Change owed: 0')
        break
    elif change < 0:
        print(f'Change owed: {abs(change)}')
        break


    print(f'Amount due: {amount_due}')
