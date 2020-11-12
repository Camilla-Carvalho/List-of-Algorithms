def metade(num=0):
    met = num / 2
    return met


def dobro(num=0):
    dob = num * 2
    return dob


def porcentagem(num=0, taxa=0):
    result = num + (num * taxa) / 100
    return result


def diminuir(num=0, taxa=0):
    result = num - (num * taxa) / 100
    return result


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
