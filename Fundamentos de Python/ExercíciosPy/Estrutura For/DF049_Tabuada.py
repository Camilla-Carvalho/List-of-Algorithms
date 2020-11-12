num = int(input('Digite um número: '))
i = 0
for i in range(0, 10):
    i = i + 1
    print(f'{num} X {i} = ', end='')
    print(num * i)
