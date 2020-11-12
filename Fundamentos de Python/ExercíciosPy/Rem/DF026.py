frase = str(input('Digite uma frase: ')).lower()
print('A letra (A) aparece {} vezes...'.format(frase.count('a')))
print('A primeira letra (A) apareceu na posição {}'.format(frase.find('a')+1)
print('A letra (A) aparece pela última vez na posição {}'.format(frase.rfind('a')+1))

