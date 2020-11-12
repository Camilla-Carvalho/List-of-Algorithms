from datetime import datetime

data_str = '2019/09/20 19:56:00'

print(datetime.strptime(data_str, '%Y/%m/%d %H:%M:%S'))