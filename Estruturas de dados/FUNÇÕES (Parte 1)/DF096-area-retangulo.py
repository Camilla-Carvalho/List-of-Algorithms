def header(txt):
    print('\nControle de terrenos')
    print('-' * 30)

def area(larg, comp):
    form = larg * comp
    print(f'A area de um terreno {larg} x {comp} = {form:.1f}m²')


# Program princpal
header('')
area(larg=float(input('Largura (m): ')), comp=float(input('Comprimento (m):')))

