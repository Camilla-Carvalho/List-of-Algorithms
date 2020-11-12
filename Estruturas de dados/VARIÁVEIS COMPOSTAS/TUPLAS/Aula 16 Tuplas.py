# print(lanche [-1]) --> inverte a lista.. podemos o primeiro elemento por [0] or [-1]
# () tupla [] lista {}dicionário
# enumerate range and for.

# Sorted -> comando para printar em ordem alfabética.



lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita') #Podemos criar uma tuplas sem parenteses.

# for comida in lanche: --> não mostra a posição a não ser:
#     print(f'Eu vou comer {comida}') #Ele vai printar cada item (comida) da lista lanche.
# print(f'Ao todo temos {len(lanche)} comidas no cardápio')

for pos, comida in enumerate(lanche): #Mostra a posição dos itens presentes na tupla
    #Enumerate me da dados e posição --> pos para posição.
    print(f'Eu vou comer {comida} na posição {pos}') #pos para posição.

# for cont in range(0, len(lanche)):  #range também ignora o ultimo valor.
#     print(f'Vou comer {lanche[cont]} na posição {cont}') #momentos em que só sai a resposta desta maneira.

#Ambos os for's tem o mesmo resultado.