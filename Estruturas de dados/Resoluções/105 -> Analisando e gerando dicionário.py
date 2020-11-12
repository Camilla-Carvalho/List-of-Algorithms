def notas(* n, sit=False):
    """

    -> Função para analisar notas e situações de vários alunos
    :param n: recebe uma ou mais notas dos alunos
    :param sit: Valores opcional dizendo a situação
    :return: Dicionário com várias situações da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


#Principal program

resp = notas(5.5, 2.5,8.5, sit=True)
print()
print(resp, notas.__doc__)