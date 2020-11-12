def parametro(txt):
    print('-'*30)
    print('SEQUÊNCIA DE FIBONACCI')
    print('-' * 30)

def sequencia(tio):
    print('~'*30)


#Transação de termo -> fazer t1 passar a ser t2 e t2 passar a ser t3
parametro('')
#Primeiros termos são definidos automaticamente
t1 = 0
t2 = 1
i = 0
termos = int(input('Digite quantos termos deseja vizualizar: '))
sequencia('')
print(f'{t1} -> {t2}', end=' -> ')
while i <= termos:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    i += 1


