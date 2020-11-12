lista = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > len(lista)-1:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem na lista foram: {lista}')
