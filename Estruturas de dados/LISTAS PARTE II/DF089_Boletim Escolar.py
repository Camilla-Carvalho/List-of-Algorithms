from time import sleep
lista = []
boletim = []
media = 0
while True:
    nome = input('Digite seu nome: ').capitalize()
    lista.append(nome)
    nota1 = float(input('Nota 1: '))
    lista.append(nota1)
    nota2 = float(input('Nota 2: '))
    lista.append(nota2)
    media = (nota1 + nota2)/2
    lista.append(media)
    ## lista.append([nome, [nota1, nota2], media])
    boletim.append(lista[:])
    lista.clear()
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]:\033[0m ').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÂO INVÁLIDA!', end='')
    if option == 'N':
        break

print('-=' * 30)
print('No. NOME         MÉDIA')
print('-' * 25)
for i, l in enumerate(boletim):
    print(f'{i:^2} {l[0]:^5} {l[3]}')
while True:
    for i, l in enumerate(boletim):
        notas = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
        if notas == len(boletim):
            print(f'Notas de {i}')
        if notas == 999:
            sleep(1)
            print('FINALIZANDO...\n')
            break
    break
print('<<< VOLTE SEMPRE >>>')
