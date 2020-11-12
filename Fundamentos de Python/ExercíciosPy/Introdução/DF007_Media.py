print('Media de alunos')
a = int(input('Type a value of first test: '))
b = int(input('Type a value of the last test: '))
mf = (a+b)/2
if mf >= 7:
    print(f'Você tirou {mf}, Parabéns, foi aprovado!')
else:
    print(f'Você tirou {mf}, Se fudeu..')