i = True
while i == True:
    lista = ['cachorro', 'gato', 'vaca', 'arara']
    animal = str(input('\033[0m\nDigite o nome do animal que pretende checar: '))
    if animal in lista:
        print('\nEste animal existe na lista! ')
    else:
        print('\nEsse animal não existe na lista, mas será adicionado! \n\033[36m')
        lista.append(animal)

    print(lista)

