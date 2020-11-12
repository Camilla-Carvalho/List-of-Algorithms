from datetime import datetime

date = input()
date = datetime.strptime(date, '%d/%m/%Y')
date_curr = datetime.strftime(date, '%Y-%m-%d')
print(date_curr)