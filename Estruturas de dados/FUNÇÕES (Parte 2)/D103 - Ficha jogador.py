def header(txt):
    print('=' * len(txt))
    print(f'{txt:^30}')
    print('=' * len(txt))


def jogo(jogador=0, gols=0):
    if not jogador:
        jogador = '<Desconhecido>'
    if not gols:
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato'
    print('-=' * 25)


header('    C A M P E O N A T O     ')
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
print(jogo(jogador, gols))
