# nesting dan multikey dictionary
import datetime  # import datetime di gunakan untuk mendapatkan tanggal dan waktu saat ini

siswa1 = {
    "nama": "Rizky",
    "umur": 20,
    "alamat": "jl. Polo Polo",
    "lahir": datetime.datetime(2007, 2, 10)
}

siswa2 = {
    "nama": "Udin",
    "umur": 22,
    "alamat": "jl. Pale Plae",
    "lahir": datetime.datetime(2000, 5, 2)
}

siswa3 = {
    "nama": "Pace",
    "umur": 24,
    "alamat": "jl. Cepace",
    "lahir": datetime.datetime(2000, 1, 1)
}

dataSiswa = {
    "data1": siswa1,
    "data2": siswa2,
    "data3": siswa3,
}

print(f"{'No. ':<10} {'Nama':<15} {'Umur':<15} {'Alamat':<15}  {'Lahir':<15}")
p = "---".center(66, '-')
print(p)

# digunakan untuk mengakses data
for siswa in dataSiswa.keys():  # keys() digunakan untuk mengakses kunci dari dictionary
    KEY = siswa
    NAMA = dataSiswa[KEY]["nama"]
    UMUR = dataSiswa[KEY]["umur"]
    ALAMAT = dataSiswa[KEY]["alamat"]
    LAHIR = dataSiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<10} {NAMA:<15} {UMUR:<15} {ALAMAT:<15}  {LAHIR:<15}")
