frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes '.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #Este +1 altera a localização
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

