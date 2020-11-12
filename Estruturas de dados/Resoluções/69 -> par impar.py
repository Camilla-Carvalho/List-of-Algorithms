from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = (jogador + computador)
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = input('Par ou impar? [P/I]: ').strip().upper()[0]
    print(f'Você jogou {jogador} e computador jogou {computador}. O total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 0 == 1:
            print('Você venceu!')
            vit
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes')