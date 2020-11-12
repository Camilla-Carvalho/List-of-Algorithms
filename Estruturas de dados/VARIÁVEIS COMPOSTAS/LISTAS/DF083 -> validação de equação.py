expressão = str(input(f'Digite uma expressão: ')) #Toda a string é uma lista// usamos o for para pegar cada letra/símbol
pilha = []
for simbolo in expressão: ##Para cada simbolo na expreção faça:
    if simbolo == '(':
        pilha.append('(')

    elif simbolo == ')': #Ou a lita está vazia ou está cheia (Pode ser que esteja no final da lista)
        if len(pilha) > 0: #Se for maior que zero significa que não está vazia
            pilha.pop() #removemos o último elemento da lista
        else:
            pilha.append(')')
            break

if len(pilha) == 0: ##Quer dizer que cada parenteses que abriu encontrou o seu par, assim satisfazendo as condições
    print('Sua expressão está válida!')
else: # Se o len da plha for maior que zero
    print('Sua expressão está errada!')

