def notas(*num, sit=False):
    """

    :param num: passa uma lista que por sua vez retornará um dicionário com as notas e sit de cada aluno
    :param sit: Parametro opcional para exibir situação do alunos (aprovado // reprovado)
    :return: retorna um dicionário com total, maior e menor nota, média e situação (opcional)
    """
    resp = {}
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    resp['media'] = sum(num) / len(num)
    if sit:
        if resp['media'] >= 7:
            resp['situação'] = 'BOA'
        elif resp['media'] >= 5:
            resp['sitação'] = 'RAOZÁVEL'
        else:
            resp['situação'] = 'RUIM'

    return resp


resposta = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resposta)
while True:
    option = ' '
    while option not in 'SN':
        option = input('Deseja vizualizar a documentação?[S/N]: \033[0m').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA! ', end='')
    if option in 'S':
        print(notas.__doc__)
        break
    if option == 'N':
        break
print('Obrigada por usar nosso programa!')
