from time import sleep
n1 = int(input('\nType a first value: '))
n2 = int(input('Type a second value: '))
option = 0
formula = 0
while option != 5:

    print('''\033[35m
    [ 1 ] sum
    [ 2 ] Multiply
    [ 3 ] Larger
    [ 4 ] New numbers 
    [ 5 ] Leave\033[0m 
    ''')
    option = int(input('choice one option: '))
    if option == 1:
        formula = (n1 + n2)
        print(f'The sum of {n1} + {n2} = {formula}')
    elif option == 2:
        formula = (n1 * n2)
        print(f'The multipication of {n1} x {n2} = {formula}')
    elif option == 3:
        if n1 > n2:
            print(f'Between {n1} and {n2} the largest number is {n1}')
        else:
            print(f'Between {n1} and {n2} the largest number {n2}')
    elif option == 4:
        print('Inform the numbers again...')
        n1 = int(input('\nType a first value: '))
        n2= int(input('Type a second value: '))
    elif option == 5:
        print('\033[34mFinishing...\033[0m')
        sleep(3)
    else:
        print('\033[31mInvalid option! Try again... \033[0m')
print('End of program.')
