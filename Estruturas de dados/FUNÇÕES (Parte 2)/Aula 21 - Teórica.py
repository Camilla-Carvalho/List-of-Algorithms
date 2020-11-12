def teste(b):
    a = 8
    b = 4
    c = 2
    print('-=' * 20, '\nVariável local: ')
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# principal program
a = 5
teste(a)
print('-=' * 20)
print(f'Variável Global\nA fora vale {a}')