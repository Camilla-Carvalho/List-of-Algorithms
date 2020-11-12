reta1 = float(input())
reta2 = float(input())
reta3 = float(input())
reta4 = float(input())
print('As retas abaixo formam um ', end='')

if reta1 == 0 or reta2 == 0 or reta3 == 0 or reta4 == 0:
    print('Não é possível formar nenhum segmento.')

elif reta1 == reta2 and reta3 == reta4 and reta1 == reta3 and reta2 == reta4:
    print('QUADRADO')
elif reta1 != reta2 and reta3 != reta4 and reta1 != reta3 and reta2 != reta4 and reta1 != reta4:
    print('QUADRILÀTERO')
else:
    print('RETÂNGULO')

