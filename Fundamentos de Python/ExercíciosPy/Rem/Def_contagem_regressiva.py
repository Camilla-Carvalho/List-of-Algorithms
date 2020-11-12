def contagem_regresiva(num):
    from time import sleep
    for i in range(21, 0, -2):
        sleep(1)
        print(i + 1)

def contagem_normal(num2):
    from time import sleep
    for i in range(0, 21, 2):
        sleep(1)
        var = i + 1
        print('\033[34m', var)

def listas(list):


#programa principal
var = 0
i = 1
contagem_normal(' ')
print('\033[31m-='*10)
contagem_regresiva('') #precisa estar entre aspas




