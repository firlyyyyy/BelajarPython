# latihan dictionary
import datetime
import os

# template siswa
siswaTemplate = {
    "nama": "nama",
    "kelas": "kelas",
    "nis": "000000",
    "jurusan": "jurusan",
    "lahir": datetime.datetime(1111, 1, 11)
}

dataSiswa = {}

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
siswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print() 