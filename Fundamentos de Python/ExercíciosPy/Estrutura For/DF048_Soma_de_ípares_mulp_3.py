soma = 0
cont = 0
for i in range(1, 501, 2):

    if i % 3 == 0:  #mltiplo é divisivel
       print(i, end=' ')
       cont = cont + 1 #Achei mais um/ Acumula valores encontrados. CONT += 1
       soma = soma + i #SOMA += I --> Mesma coisa dele receber ele mesmo mais "i"
print(f'\nA soma dos {cont} números ímpares múltipos de três encontrados é: {soma}')