tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez') #No mãximo oitenta colunas

# while numero > 10 or numero < 0:
while True:
    numero = int(input('Digite um número entre 0 e 5:\033[0m '))
    if 0 <= numero <= 10:
        break
    print('\033[31mOPÇÃO INVÁLIDA! ', end='')
print(f'Você digitou o número {tupla[numero]}') #A palavra estará na posição [i] da tupla





