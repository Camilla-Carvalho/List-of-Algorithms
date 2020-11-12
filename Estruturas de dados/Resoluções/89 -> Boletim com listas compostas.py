from time import sleep
lista = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/ 2
    lista.append([nome, [nota1, nota2], media])
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar? [S/N]: \033[0m').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA!', end='')
    if option == 'N':
        break
print(print('-=' * 30))
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>3}')
print('-' * 26)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10} {aluno[2]:<10.1f}')
print('-=' * 25)
while True:
    print('-' * 30)
    option = int(input('Mostrar notas de quais alunos?(999 para sair): '))
    if option == 999:
        print('\nFINALIZANDO...')
        sleep(3)
        break
    if option <= len(lista) -1:
        print(f'Notas de {lista[option][0]} são {lista[option][1]}')
        #for indice, aluno in enumerate(lista):
         #   print(f'O aluno(a): {aluno[0]} tirou {aluno[1][0]} e {aluno[1][1]}')
print('<<< VOLTE SEMPRE >>>')
