a = [2, 4, 6, 8]
b = a

b[2] = 12  ## As listas em python trabalham com ligação "Efeito espelho"...
#O que alterar em uma lista identica atribuída, irá influenciar direto na outra.

print(f'Lista A: {a}\nLista B: {b}')

b = a[:] #Cópia simples \\ Pede todos os elementos de A.
b = a #Copia e cria uma ligação.
