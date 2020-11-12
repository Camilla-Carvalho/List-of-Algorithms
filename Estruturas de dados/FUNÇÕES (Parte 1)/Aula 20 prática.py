# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1
#
#
# valores = [6, 3, 6, 1, 0, 2]
# dobra(valores)
# print(valores)

# =================================================================================================================
# def soma(a, b):
#     s = a + b
#     print(f'A= {a} e B = {b}\nA soma de {a} + {b} = {s}')
#
#
#
# # Program Principal
# soma(a=int(input('Digite o primeiro valor: ')), b=int(input('Digite o segundo valor: ')))
# soma(a=int(input('Digite o primeiro valor: ')), b=int(input('Digite o segundo valor: ')))
# soma(a=int(input('Digite o primeiro valor: ')), b=int(input('Digite o segundo valor: ')))

# ==================================================================================================================
# def contador(* var):
#     tamanho = len(var)
#    print(f'Recebi os valores {var} e são ao // todo {tamanho}')
# # programa principal
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# ==================================================================================================================

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
    pos += 1


# program principal
value = [7, 2, 5, 0, 4]
dobra(value)
print(value)


