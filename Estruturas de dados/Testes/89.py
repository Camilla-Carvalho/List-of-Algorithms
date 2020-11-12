from time import sleep
lista = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar? [S/N]: \033[0m').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA!' ,end='')
    if option in 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 26)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:<8.1f}')
while True:
    option = int(input('De quais alunos deseja ver a nota? (999 para sair): '))
    if option == 999:
        print('\nFINALIZANDO...')
        sleep(3)
        break
    if option <= len(lista) -1:
        print(f'As notas de {lista[option][0]} são {lista[option][1][0]} e {lista[option][1][1]}')
print('<<< VOLTE SEMPRE >>>')




