# def pangkat(angka, pangkat):
#     hasil = angka ** pangkat
#     print(f"hasil dari {angka} pangkat {pangkat} adalah = {hasil}")
# pangkat(
#     int(input("masukkan angka: ")),
#     int(input("masukkan pangkat: ")),
# )

""" MODULE """
from contohModule1 import tambah, kali  # cara menggunakan from

tambah(1, 2, 3, 5, 7, 3, 1, 1)
kali(3, 3)

# bisa juga menggunakan as
from  contohModule1 import tambah as t, kali as k  # cara menggunakan as atau kata ganti 

t(1, 1, 1, 1, 1, 1, 1)
k(1, 1, 1, 1, 1, 1, 1)