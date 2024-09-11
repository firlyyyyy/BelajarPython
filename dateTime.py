# date and time

import locale
import datetime as dt
# import random

# tebakAngka = random.randint(0, 20)
# angka = int(input("masukkan angka 1 - 20: "))

# hasil = ["benar!!", "yahh salah"][angka != tebakAngka]
# print(hasil)

hari = dt.date.today()
print(hari)
print("ini hari {:%A}".format(hari), "\n")

judul = "TANGGAL LAHIR".center(25, "-")
print(judul)

locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')  # untuk mengatur hari menjadi bahasa indonesia

nama = input("masukkan nama\t\t\t\t: ")
tanggal = int(input("masukkan tanggal\t\t\t: "))
bulan = int(input("masukkan bulan\t\t\t\t: "))
tahun = int(input("masukkan tahun\t\t\t\t: "))

lahir = dt.date(tahun, bulan, tanggal)
print(f"nama anda {nama}, tanggal lahir anda\t: {lahir:%A}, {lahir}")

hari_ini = dt.date.today()
umur = hari_ini - lahir
umurTahun = umur.days // 365
umurBulan = (umur.days % 363) // 30
print(f"umur anda\t\t\t\t: {umurTahun} tahun, {umurBulan} bulan")

# data = int(input("masukkan angka: "))

# hasil = ['genap', 'ganjil'][data % 2]
# print(hasil)