##Não usar acentos em tuplas

Lista_de_Palavras = ('Aprender', 'Comer', 'Linguagem', 'Python', 'Programar', 'Futuro', 'Trabalho', 'Amor')

for palavra in Lista_de_Palavras:
    print(f'\n\nNa palavra \033[34m{palavra.upper()}\033[0m temos: ', end='')
    for letra in palavra: ##Toda a string já é uma lista.
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')

