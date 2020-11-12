def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16 and idade:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade <= 16 > 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
nascimento = int(input('Digite o ano em que nasceu: '))
print(voto(nascimento))