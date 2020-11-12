num_int = int(input('Type a value: '))
u = num_int // 1 % 10
d = num_int // 10 % 10
c = num_int // 100 % 10
m = num_int // 1000 % 10
print(f'Analisando o número {num_int}')
print(f'Unidade: {u}',end=' ')
print(f'Dezena: {d}',end=' ')
print(f'centena: {c}',end=' ')
print(f'Milhar: {m}')