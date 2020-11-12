def jogo(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')

nome = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    jogo(gols=gol)
else:
    jogo(nome, gol)
