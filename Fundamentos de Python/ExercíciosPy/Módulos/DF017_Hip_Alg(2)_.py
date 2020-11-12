import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o compimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print(f'A hipotenusa dos catetos é {hi:.2.f}')
