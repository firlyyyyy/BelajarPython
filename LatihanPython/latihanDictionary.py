# latihan dictionary
import datetime
import os
import string
import random

# template siswa
siswaTemplate = {
    "nama": "nama",
    "kelas": "kelas",
    "nis": "000000",
    "jurusan": "jurusan",
    "lahir": datetime.datetime(1111, 1, 11)
}

dataSiswa = {}

while True:
    os.system("clear")  # digunakan untuk membersihkan layar
    p = "DATA SISWA".ljust(40, "-")
    print(p)

    siswa = dict.fromkeys(siswaTemplate.keys())  # digunakan untuk membuat dictionary baru dengan key yang sama dengan dictionary yang sudah ada
    siswa['nama'] = input("masukkan nama: ")
    siswa['kelas'] = input("masukkan kelas: ")
    siswa['nis'] = input("masukkan nis: ")
    siswa['jurusan'] = input("masukkan jurusan: ")
    TAHUN_LAHIR = int(input("masukkan tahun lahir: "))
    BULAN_LAHIR = int(input("masukkan bulan lahir: "))
    TANGGAL_LAHIR = int(input("masukkan tanggal lahir: "))
    print("\n")
    siswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = "".join(random.choice(string.ascii_uppercase) for i in  range(5))
    dataSiswa[KEY] = siswa

    print(f"{"KEY":<10} {"Nama":<10} {"Kelas":<10} {"NIS":<10} {"Jurusan":<10} {"Lahir":<10}")
    print("-"*75) 

    for key, data in dataSiswa.items():
        # KEY = siswa
        NAMA = data["nama"]
        KELAS = data["kelas"]
        NIS = data["nis"]
        JURUSAN = data["jurusan"]
        LAHIR = data["lahir"].strftime("%x")
        
        print(f"{KEY:<10} {NAMA:<10} {KELAS:<10} {NIS:<10} {JURUSAN:<10} {LAHIR:<10}")
        
    tambahData = input("apakah ingin menambah data? (y / n): ")
    if tambahData == "n":
        break

print("terima kasih.....")
    