frase = '  Curso em vídeo python '
print(frase.replace('python','android')) # Troca uma palavra por outra

print(frase[::])

print(frase.upper().count('O')) # Conta a quatidade de 'O' minúsculo, convertidos em maiusculos

print(len(frase.strip())) #Conta a quantidade de caracteres, incluindo espaço
# Se adicionarmos o strip, os espaços r l serão desconsiderados
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('curso'))

print(frase.split())


