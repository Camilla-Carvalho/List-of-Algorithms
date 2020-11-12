frase = str(input('Digite uma frase: ')).strip().upper()
nova_frase = frase.split()
frase_junta = ''.join(nova_frase)
inverso = '' #Não pode ser um valor

for i in range(len(frase_junta)-1, -1, -1):
    inverso += frase_junta[i]
print(f'O inverso de {frase_junta} é {inverso}')
if inverso == frase_junta:
    print('Temos um palíndomo!')
else:
    print('Essa frae não é um palíndromo')