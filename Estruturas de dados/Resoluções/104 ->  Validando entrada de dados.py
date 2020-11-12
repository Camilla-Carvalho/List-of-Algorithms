def leiaInt(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[31mOPÇÃO INVÁLIDA! Por favor digite um número inteiro.\033[0m')
        if ok:
            break
    return value


num = leiaInt('Digite um número: ')
print(f'O número digitado foi {num} ')