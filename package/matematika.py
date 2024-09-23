""" MODULE MATEMATIKA """

def tambah(*args):
    """ Menghitung hasil penjumlahan dari beberapa angka """
    hasil = 0
    for data in args:
        hasil += data
    return hasil


def kali(*args):
    """ Menghitung hasil perkalian dari beberapa angka """
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

def pangkat(angka, pangkat):
    return angka ** pangkat