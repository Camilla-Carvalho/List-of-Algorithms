# def fatorial(num=1):
#     f = 1
#     for i in range(num, 0, -1):
#         f *= i
#     return f
#
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
#
# print(f'Os resultados são {f1}, {f2} e {f3}')


def Par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if Par(num):
    print(f'{Par(num)}! {num} É par.')
else:
    print(f'{Par(num)}! {num} Não é par.')