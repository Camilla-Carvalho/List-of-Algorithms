

lista_de_Palavras = ('Aprender', 'Comer', 'Linguagem', 'Python', 'Programar', 'Futuro', 'Trabalho', 'Amor')

for palavra in lista_de_Palavras:
    print(f'\nNa palavra \033[34m{palavra.upper()}\033[0m temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\033[34m{letra}\033[0m', end=' ')

