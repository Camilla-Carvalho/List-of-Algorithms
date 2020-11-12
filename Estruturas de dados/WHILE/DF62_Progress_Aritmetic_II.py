def mensagem(txt):
    print('Gerador de PA')
    print('=-' * 16)


#programa principal
print('\n======PROGRESSÃO ARITMÉTICA======')
mensagem('')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'Você usou {cont-1} termos no total')





