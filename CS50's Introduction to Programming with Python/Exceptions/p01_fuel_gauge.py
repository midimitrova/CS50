from math import ceil, floor

while True:
    try:
        x,y = input('How much fuel is in a tank? ').split("/")
        x = int(x)
        y = int(y)
        result = (x / y)
        if x > y:
            x, y = input('How much fuel is in a tank? ').split("/")

    except (ValueError):
        print('x and y are not integers!')
    except ZeroDivisionError:
        print('You can not divide by zero!')
    except:
        pass
    else:
        if result <= 0.01:
            print('E')
        elif result >= 0.99:
            print('F')
        else:
            print(f'{round(result*100)}%')
        break

