def mensagem(txt):
    print('Gerador de PA')
    print('=-' * 16)


#Programa principal
print('\n======PROGRESSÃO ARITMÉTICA======')
mensagem('')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    cont += 1
print('FIM')

