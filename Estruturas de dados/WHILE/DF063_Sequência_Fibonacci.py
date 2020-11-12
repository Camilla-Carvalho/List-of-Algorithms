def cabecalho(txt):
    print('-'*30)
    print('SEQUÊNCIA DE FIBONACCI')
    print('-' * 30)

cabecalho('')
termos = int(input('Digite a quantidade de vezes que deseja vizualizar a sequência: '))
print('~'*30)
#Os primeiros termos de uma sequência de Fibonacci sempre começam com '0' e '1' por padrão
t1 = 0
t2 = 1
i = 3 #variavel armazenamento // Como t1 e t2 já foram declarados,  o contador deve ser inicializado em 3
print(f'{t1} -> {t2}', end=' -> ')
while i <= termos:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    i += 1
print('FIM')
print('~'*30)


