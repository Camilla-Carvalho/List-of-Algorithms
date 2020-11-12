from datetime import datetime

curr_datetime = datetime.now() # Printará as funções de data e hora em tempo real do momento execução.
curr_date = curr_datetime.date() # Printará somente a data na tela
curr_time = curr_datetime.time()# Printará somente o horário com os milésimos de segundo do momento de execução.

print(curr_datetime)
print(curr_date)
print(curr_time)
