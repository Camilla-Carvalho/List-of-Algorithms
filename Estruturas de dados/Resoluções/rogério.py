def header(txt):
    print('='*30)
    print(txt)
    print('=' * 30)

def notas():
    soma = 0
    boletim['nome'] = input('Nome: ')
    boletim['nota1'] = int(input('Primeira nota: '))
    soma += boletim['nota1']
    boletim['nota2'] = int(input('Segunda nota: '))
    soma += boletim['nota2']
    boletim['nota3'] = int(input('Terceira nota: '))
    soma += boletim['nota3']
    boletim['nota4'] = int(input('Quarta nota: '))
    soma += boletim['nota4']
    media = soma / len(boletim)
    print(media)

#programa principal
header(f'{"B O L E T I M":^30}')
boletim = {}
lista = []
notas()












