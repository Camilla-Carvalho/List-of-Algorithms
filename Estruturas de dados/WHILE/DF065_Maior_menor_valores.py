
cont = soma = media = maior = menor = 0
option = 'S'
while option[0].upper() in 'sS':

    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num #por ser o primeiro número da condição, automaticamente será maior e menor.
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    option = input('Deseja continuar? [S/N]: ').strip()
media = (soma / cont)
print(f'Você digitou {cont} números e media foi {media}\nO maior deles é {maior} e o menor é {menor}')
print('Acabou')
