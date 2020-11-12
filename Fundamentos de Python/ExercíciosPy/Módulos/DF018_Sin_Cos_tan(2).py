from math import sin, tan, cos, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O angulo de seno é: {seno:.2f}\n O Cosseno é {cos:.2f}\n A tangente é {tang:.2f}')
