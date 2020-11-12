estado = {}
brasil = []
for i in range(0, 3):
    estado['uf'] = input('Digite a União Federativa: ').capitalize()
    estado['sigla'] = input('Digite a sigla: ').upper()
    brasil.append(estado.copy()) #Se não fizer uma cópia o ultimo item irá sobrescrever os anteriores.
print(brasil)
for estate in brasil:
    for key, value in estate.items():
        print(f'O campo {key} tem o valor {value}')
