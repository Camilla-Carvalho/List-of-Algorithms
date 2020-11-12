from time import sleep

# Lista global. Podemos utiliza-la no programa inteiro
cores = ('\033[m',         # 0 - without color
         '\033[0;30;41m',  # 1 - background red
         '\033[0;30;42m',  # 2 - background green
         '\033[0;30;43m',  # 3 - background yellow
         '\033[0;30;44m',  # 4 - background blue
         '\033[0;30;45m',  # 5 - background purple
         '\033[7;30m',     # 6 - background white
         );


def ajuda(comand):
    """
    :param comand:  recebe o comando que será feita a consulta
    :return: retorna o manual da função consultada
    """
    title(f'Acessando o manual do comando \'{comand}\'', 4)
    print(cores[6], end='')
    help(comand)
    print(cores[0], end='')
    sleep(2)


def title(msg, cor=0):
    """
    :param msg: Exibe mensagem de interação com usuário
    :param cor: cores de fundo das mensagens exibidas para o usuário
    :return: retorna uma mensagem seguida de uma cor de fundo para melhor distinção.
    """
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(1)


# principal program
comando = ' '
while True:
    title('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
title('ATÉ LOGO', 1)
