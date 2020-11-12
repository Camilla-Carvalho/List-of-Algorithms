reta1 = float(input('Primeira reta: '))
reta2 =  float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2: #Ordem numérica
    print('Os seguimentos acima podem formar um triangulo ', end='')

    if reta1 == reta2 and reta2 != reta3:
        print('\033[34mISÓCELES')

    elif reta2 == reta3 and reta3 != reta1:
        print('\033[34mISÓCELES')

    elif reta1 == reta3 and reta2 != reta1:
        print('\033[34mISÓCELES')

    elif reta1 == reta2 and reta1 == reta3: #r1 == r2 == r3
            print('\033[34mEQUILÁTERO!')
    else:
            print('\033[34mESCALENO')  #r1 != r2 != r3 != r1
else:
     print(f'\n\033[31m{reta1}, {reta2} e {reta3} não podem formar um triângulo.')
