ano = int(input('\033[35m Digite o ano que deseja analisar, ou tecle zero para analizar o ano atual: '))
print(''
      ''
      '')
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[034m O ano {ano} é BISSEXTO!!')
else:
    print(f'\033[31m O ano {ano} NÃO é BISSEXTO')