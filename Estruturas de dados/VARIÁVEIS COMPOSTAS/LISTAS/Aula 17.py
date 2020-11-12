from random import randint
num = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)  #primeiro indicamos a posição e depois o número que desejamos inserir
num.pop()
print(num)
if 4 in num:
    num.remove(4) #Percorre a lista e elimina a primeira ocorrência.
    print('Primeiro número quatro removido! ')
else:
    print('Não achei o número 4')

print(f'Essa lista tem {len(num)} elementos')