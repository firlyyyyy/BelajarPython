""" MEMBACA FILE EXTERNAL """
p = " MEMBACA FILE EXTERNAL ".center(30, "=")
print(p)

file = open("ReadFileExternal/data.txt", mode="r") 
print(f"status read: {file.readable()}")  # digunakan untuk mengecek status file apakah masih bisa dibaca atau tidak
print(f"status write: {file.writable()}\n")  # digunakan untuk mengecek status file apakah masih bisa ditulis atau tidak

""" BACA SELURUH FILE """
# print(file.read())  # digunakan untuk membaca file

""" BACA FILE PER BARIS """
print(file.readline(), end="")  # membaca baris pertama file, end="" -> untuk menghilangkan enter
print(file.readline(), end="")  # membaca baris kedua file, end="" -> untuk menghilangkan enter

""" BACA FILE SEBAGAI LIST """
# print(file.readlines())

file.close()  # digunakan untuk menutup file agar tidak terjadi error
print("\n")

""" TEKNIK MEMBACA FILE EXTERNAL MENGGUNAKAN WITH """
p = " MEMBACA FILE EXTERNAL DENGAN WITH ".center(50, "=")
print(p)

# with digunakan untuk membuka file dan menutupnya secara otomatis
with open("ReadFileExternal/data.txt", mode="r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")