## membuat exception sendiri
from numbers import Number
import os

os.system("clear")
def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "input harus angka"
    return a + b
print(f"hasil = {tambah(9, 2)}")

angka = 0

## cara 1
# try:
#     hasil = 10 / angka
# except Exception as error_message:
#     print(error_message)

## cara 2
try:
    hasil = 10 / angka
except ZeroDivisionError as error_message:
    print(error_message)