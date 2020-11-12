primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao #enésimo termo de uma pa
for i in range(primeiro_termo,decimo,razao):
    print(f'{i}',end='->')