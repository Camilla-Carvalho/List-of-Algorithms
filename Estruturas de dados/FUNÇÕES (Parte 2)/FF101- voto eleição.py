

def voto(data):
    from datetime import datetime

    data_atual = datetime.now().year
    idade = data_atual - data
    retorno = ' '

    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o vito é: Opcional'
    elif idade > 16:
        return f'Com {idade} anos o voto é: Negado'
    else:
        return f'Com {idade} anos o voto é: Obrigatorio'


# Principal program
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
