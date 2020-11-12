from datetime import datetime
date = input()
date = datetime.now()
date_curr = datetime.strftime(date, '%Y/%/%d')
print(date_curr)