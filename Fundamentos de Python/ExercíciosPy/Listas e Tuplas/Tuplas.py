#Diferença de uma Tupla para uma lista Tupla = Imutável // lista = mutável

lista = [2, 5, 1, 4]
lista_animal = ['cachorro', 'gato', 'leão', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14) #Tupla é lista, mas entre parenteses
print(tupla)
print(len(tupla))
tuple_animal = tuple(lista_animal)
print(type(tuple_animal))
print(tuple_animal)