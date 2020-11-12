def factorial(value=1, show=False):
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
    print('-=' * 30)



num = int(input('Type a value: '))
print(factorial(num, show=True))