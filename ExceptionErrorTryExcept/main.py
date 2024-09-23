"""exception akan terjadi saat program mengalami error saat runtime"""

from math import nan
## contoh sederhana untuk menangkap exception

# inputUser = int(input("masukkan angka: "))
# hasil = nan

# try:
#     hasil = 10 / inputUser
# except:
#     print("input tidak boleh 0")
    
# print(f"hasil = {hasil}")

## contoh jika di aplikasikan
# contoh 1
while True:
    angka = int(input("masukkan angka: "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        done = input("apakah ingin lanjut? (y/n) ")
        if done == "n":
            break
    except:
        print("jika angka 0, masukkan angka lain: ")
print("akhir program 1")

# contoh 2
while True:
    try:
        with open("ExceptionErrorTryExcept/data.txt", mode="r") as file:
            print(file.read())
        break
    except:
        print("file tidak ditemukan, akan membuat file baru")
        with open("ExceptionErrorTryExcept/data.txt", mode="w", encoding="utf-8") as file:
            file.write("data baru")
        break
            
print("akhir program 2")