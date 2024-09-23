import datetime

data_waktu = datetime.datetime.now()
print(data_waktu)
print(data_waktu.year)
print(data_waktu.hour)
print(data_waktu.strftime('%A'))
print(data_waktu.minute)
print(data_waktu.fold)

from collections import Counter
data = ['a', 'a', 'a', 'a', 'a', 'n', 'n', 'n', 'n', 'n']

data_count = Counter(data)
print(data_count['a'])

import io

file = io.open("text.txt", "r")
print(file.read())
