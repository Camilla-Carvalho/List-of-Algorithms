def cabecalho(tit):
    print('='*30)
    print('SEQUENCIA DE FIBONACCI')
    print('='*30)


cabecalho('')
termo = int(input('Digite até que termo deseja vizualizar a sequência: '))
t1 = 0
t2 = 1
i = 2
print(f'{t1} -> {t2}', end=' -> ') #Fica do lado de fora do laço.
while i < termo:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    i += 1
print('FIM')
