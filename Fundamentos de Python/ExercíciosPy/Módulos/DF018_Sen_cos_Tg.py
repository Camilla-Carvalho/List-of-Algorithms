import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f'O angulo de seno é: {seno:.2f}\n O Cosseno é {cos:.2f}\n A tangente é {tang:.2f}')

