lista = [1, 2, 4, 6, 8] #Manter listas da mesma classe
lista_animais = ['cachorro', 'gato', 'cavalo', 'andorinha', 'pavão']
soma = 0
for i in lista:
    print(i) #print(Lista_animais) printará a lista toda na mesma quantidade de itens quw há dentro da lista
# print(i) printará cada item da lista.
    soma += i
print(f'A soma dessa lista é {soma}')

#print(sum(lista)) faz a soma das listas
#print(max(lista)) faz a busca pelo maior valor da lista
#print(min(lista)) Faz busca pelo menor valor da lista

#É possível fazer esa mesma busca com listas de strings (Por ordem alfabética)

if 'lobo' in lista_animais:
    print('Existe')
else:
    print('Não existe lobo na lista, mas será incluido')
    lista_animais.append('lobo') #.append() Inclui um novo objeto a lista
    print(lista_animais)
lista_animais.pop(0) #.pop()sem parâmetros retira sempre o ultimo objeto da lista // Dentro do parenteses posso escolher o que vou tirar da ista
print(lista_animais)

#Lista_animais.remove('elefante') --> retira item específico já conhecido.