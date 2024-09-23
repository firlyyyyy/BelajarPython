def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
    print(f"hasil tambah = {hasil}")
# tambah(3, 4, 5, 2, 5, 1)

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    print(f"hasil kali = {hasil}")
