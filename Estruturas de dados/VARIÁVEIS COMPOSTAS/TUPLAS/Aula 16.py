# a = (2, 5, 4)
# b = ( 5, 8, 1, 2)
# c = a + b
# print(c)  #mescla as duas tuplas. // A ordem dos fatores altera o produto para tuplas.
# print(c.index(8))

# pessoa = ('Camilla', 18, 'f', 71.0)
# del(pessoa)  ##del deleta qualquer resquício da existência de uma variável na memória.
# print(pessoa)
#Não é possível deletar somente um item da tupla. mas é possível deletar a tupla inteira.

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:  #Ao invés de números, ele funciona com os valores dentro da tupla
    print(f'Eu vou comer {comida}')
