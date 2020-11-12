frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
concatena = ''.join(palavra)
inverso = concatena[::-1]

#for i in range(len(concatena) -1, -1, -1):
 #   inverso += concatena[i]
print(f'O inverso de {concatena} é {inverso}')
if inverso == concatena:
    print('Temos um Palíndromo!')
else:
    print('Essa frase não é palíndromo')